from rest_framework import serializers

from bulletins.models import Bulletin


class BulletinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bulletin
        fields = ('id', 'title', 'content')
