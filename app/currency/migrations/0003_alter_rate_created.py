# Generated by Django 3.2.7 on 2021-10-29 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
