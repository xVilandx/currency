from django.db import models


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=60)
    subject = models.CharField(max_length=30)
    message = models.TextField()
