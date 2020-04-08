from rest_framework import serializers

from priorities.models import Priority


class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = ('id', 'name', 'description','color','order','is_deleted')
