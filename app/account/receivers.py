from account.models import User

from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=User)
def user_pre_save_email_field(sender, instance, **kwargs):
    if instance.email:
        instance.email = instance.email.lower()


@receiver(pre_save, sender=User)
def user_pre_save_phone_field(sender, instance, **kwargs):
    if instance.phone:
        phone = ''.join([i for i in instance.phone if i.isdigit()])
        instance.phone = phone
