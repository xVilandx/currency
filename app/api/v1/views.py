from currency.models import ContactUs, Rate, Source
from currency import model_choices as mch, consts

from django_filters import rest_framework as filters
from django.core.cache import cache

from rest_framework import filters as rest_framework_filters
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import ContactUsFilter, RateFilter
from .pagination import RatePagination
from .serializer import ContactUsSerializer, RateSerializer, SourceSerializer
from .throttles import AnonCurrencyThrottle


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all().order_by('-created')
    serializer_class = RateSerializer
    pagination_class = RatePagination
    filterset_class = RateFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    ordering_fields = ['id', 'created', 'buy', 'sale']
    throttle_classes = [AnonCurrencyThrottle]
    # renderer_classes = (JSONRenderer, YAMLRenderer, XMLRenderer)
    # http_method_names = ['get', 'post', 'head', 'options', 'put', 'patch']


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    filter_backends = [rest_framework_filters.SearchFilter]
    search_fields = ['name', 'source_url']


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all().order_by('-created')
    serializer_class = ContactUsSerializer
    filterset_class = ContactUsFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    ordering_fields = ['id', 'created', 'reply_to', 'name']


class LatestRatesView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        latest_rates = cache.get(consts.LATEST_RATE_KEY)
        if latest_rates is not None:
            return Response({'rates': latest_rates})

        latest_rates = []
        for source_obj in Source.objects.all():
            for currency_type in mch.RateTypeChoices:
                latest_rate = Rate.objects \
                    .filter(type=currency_type, source=source_obj) \
                    .order_by('-created') \
                    .first()
                if latest_rate:
                    latest_rates.append(RateSerializer(latest_rate).data)

        cache.set(consts.LATEST_RATE_KEY, latest_rates, 60 * 60 * 24 * 7)
        return Response({'rates': latest_rates})
