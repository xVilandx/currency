from currency.forms import RateForm, SourceForm
from currency.models import ContactUs, Rate, Source

from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


def rate_list(request):

    rates = Rate.objects.all()
    context = {
        'rates': rates,
    }
    return render(request, 'rate_list.html', context)


def rate_details(request, pk):
    rate = get_object_or_404(Rate, id=pk)
    context = {
        'rate': rate
    }
    return render(request, 'rate_details.html', context)


def rate_create(request):
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == "GET":
        form = RateForm()

    context = {
        'form': form
    }
    return render(request, 'rate_create.html', context)


def update_rate(request, pk):

    rate = get_object_or_404(Rate, id=pk)

    if request.method == 'POST':
        form = RateForm(request.POST, instance=rate)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == "GET":
        form = RateForm(instance=rate)

    context = {
        'form': form
    }
    return render(request, 'rate_update.html', context)


def delete_rate(request, pk):
    rate = get_object_or_404(Rate, id=pk)

    if request.method == 'GET':
        context = {
            'object': rate
        }
        return render(request, 'rate_delete.html', context)
    elif request.method == 'POST':
        rate.delete()
        return HttpResponseRedirect('/rate/list/')


def source_list(request):

    sources = Source.objects.all()
    context = {
        'sources': sources,
    }
    return render(request, 'source_list.html', context)


def source_details(request, pk):
    source = get_object_or_404(Source, id=pk)
    context = {
        'source': source
    }
    return render(request, 'source_details.html', context)


def source_create(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list/')
    elif request.method == "GET":
        form = SourceForm()

    context = {
        'form': form
    }
    return render(request, 'source_create.html', context)


def update_source(request, pk):

    source = get_object_or_404(Source, id=pk)

    if request.method == 'POST':
        form = SourceForm(request.POST, instance=source)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list/')
    elif request.method == "GET":
        form = SourceForm(instance=source)

    context = {
        'form': form
    }
    return render(request, 'source_update.html', context)


def delete_source(request, pk):
    source = get_object_or_404(Source, id=pk)

    if request.method == 'GET':
        context = {
            'object': source
        }
        return render(request, 'source_delete.html', context)
    elif request.method == 'POST':
        source.delete()
        return HttpResponseRedirect('/source/list/')


def contact_list(request):

    contacts = ContactUs.objects.all()
    context = {
        'contacts': contacts,
    }
    return render(request, 'contact_list.html', context)
