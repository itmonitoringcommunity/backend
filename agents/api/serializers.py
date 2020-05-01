from rest_framework import serializers

from agents.models import Agent


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ('id', 'name', 'description', 'path',
        'script_content','script_inputs',
        'delay','output','result',
        'start_time','is_scheduled','is_deleted')
