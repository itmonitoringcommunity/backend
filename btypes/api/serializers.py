from rest_framework import serializers

from btypes.models import BType


class BTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BType
        fields = ('id', 'title', 'content')
