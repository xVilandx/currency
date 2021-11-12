from currency import model_choices as mch

from django.db import models


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    type = models.PositiveSmallIntegerField(    # noqa: A003
        choices=mch.RateTypeChoices.choices,
        default=mch.RateTypeChoices.USD,
    )
    source = models.CharField(max_length=25)


class ContactUs(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    reply_to = models.EmailField()
    subject = models.CharField(max_length=128)
    body = models.CharField(max_length=1024)
    raw_content = models.TextField()


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)


class RequestResponseLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    request_method = models.CharField(max_length=16)
    path = models.CharField(max_length=255)
    time = models.PositiveSmallIntegerField()
