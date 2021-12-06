from currency import model_choices as mch

from django.db import models
from django.templatetags.static import static


def logo_upload_to(instance, filename):
    return f'logo/{instance.name}/{filename}'


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    type = models.PositiveSmallIntegerField(    # noqa = A003
        choices=mch.RateTypeChoices.choices,
        default=mch.RateTypeChoices.USD,
    )
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE)


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
    code_name = models.CharField(max_length=64, unique=True)
    logo = models.FileField(
            upload_to=logo_upload_to,
            default=None,
            null=True,
            blank=True
        )

    @property
    def logo_url(self):
        if self.logo:
            return self.logo.url
        return static('images/logo.jpg')

    def __str__(self):
        return self.name


class RequestResponseLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    request_method = models.CharField(max_length=16)
    path = models.CharField(max_length=255)
    time = models.PositiveSmallIntegerField()
