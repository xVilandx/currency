from currency.models import ContactUs, Rate, Source

from django_filters import rest_framework as filters

from rest_framework import filters as rest_framework_filters
from rest_framework import viewsets

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
