from currency.models import Rate

from django.http.response import HttpResponse


def rate_list(request):

    results = []
    rates = Rate.objects.all()

    for rate in rates:
        results.append(
            f'ID: {rate.id}, sale: {rate.sale}, buy: {rate.buy}, created: {rate.created}, source: {rate.source}<br>')

    return HttpResponse(str(results))
