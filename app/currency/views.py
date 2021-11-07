from currency.forms import RateForm, SourceForm
from currency.models import ContactUs, Rate, Source

from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView,
    DetailView, ListView,
    TemplateView, UpdateView,
)


class IndexView(TemplateView):
    template_name = 'index.html'


class RateListView(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'


class RateCreateView(CreateView):
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_create.html'


class RateUpdateView(UpdateView):
    form_class = RateForm
    model = Rate
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_update.html'


class RateDetailsView(DetailView):
    model = Rate
    template_name = 'rate_details.html'


class RateDeleteView(DeleteView):
    model = Rate
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('currency:rate-list')


class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'


class SourceCreateView(CreateView):
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_create.html'


class SourceUpdateView(UpdateView):
    form_class = SourceForm
    model = Source
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_update.html'


class SourceDetailsView(DetailView):
    model = Source
    template_name = 'source_details.html'


class SourceDeleteView(DeleteView):
    model = Source
    template_name = 'source_delete.html'
    success_url = reverse_lazy('currency:source-list')


class ContactListView(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'contact_list.html'
