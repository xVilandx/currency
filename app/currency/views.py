from django.shortcuts import render
from django.http.response import HttpResponse

from currency.models import ContactUs


def contact_list(request):

    result = []
    all_objects = ContactUs.objects.all()
    for contact in all_objects:
        result.append(f'Email_from = {contact.email_from}, Subject = {contact.subject}, Message = {contact.message}<br>')

    return HttpResponse(result)

