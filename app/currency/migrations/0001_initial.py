# Generated by Django 3.2.7 on 2021-10-05 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_from', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=30)),
                ('message', models.TextField()),
            ],
        ),
    ]
