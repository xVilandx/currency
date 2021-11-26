from currency.forms import RateForm, SourceForm
from currency.models import ContactUs, Rate, Source

from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView,
    DetailView, ListView,
    TemplateView, UpdateView,
)


class IndexView(TemplateView):
    template_name = 'index.html'


class RateListView(ListView):
    queryset = Rate.objects.all().select_related('source')
    template_name = 'rate_list.html'


class RateCreateView(CreateView):
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_create.html'


class RateUpdateView(UserPassesTestMixin, UpdateView):
    form_class = RateForm
    model = Rate
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_update.html'

    def test_func(self):
        return self.request.user.is_superuser


class RateDetailsView(UserPassesTestMixin, DetailView):
    model = Rate
    template_name = 'rate_details.html'

    def test_func(self):
        return self.request.user.is_superuser


class RateDeleteView(UserPassesTestMixin, DeleteView):
    model = Rate
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('currency:rate-list')

    def test_func(self):
        return self.request.user.is_superuser


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


class ContactUsCreateView(CreateView):
    model = ContactUs
    template_name = 'contactus_create.html'
    success_url = reverse_lazy('index')
    fields = (
        'name',
        'reply_to',
        'subject',
        'body',
    )

    def _send_email(self):
        subject = 'User ContactUs'
        body = f'''
             Request From: {self.object.name}
             Email to reply: {self.object.reply_to}
             Subject: {self.object.subject}

             Body: {self.object.body}
         '''
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_email()
        return redirect
