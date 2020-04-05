from rest_framework import serializers

from mails.models import Mail


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = ('id', 'name', 'description','smtp','port','username','password','tolist',
        'cclist','bcclist','is_deleted')
