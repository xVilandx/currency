from currency.models import ContactUs, Rate, Source
from currency.tasks import send_email_in_background

from rest_framework import serializers


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'sale',
            'buy',
            'created',
            'source',
            'type',
        )


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'id',
            'source_url',
            'name',
            'code_name',
        )


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'id',
            'name',
            'reply_to',
            'subject',
            'body',
        )

    def create(self, validated_data):
        subject = ' User ContactUs'
        body = f'''
            Request From: {validated_data['name']}
            Email to reply: {validated_data['reply_to']}
            Subject: {validated_data['subject']}
            Body: {validated_data['body']}
                '''
        send_email_in_background.delay(
            subject,
            body,
        )
        return super().create(validated_data)
