from rest_framework import serializers,fields

from bulletins.models import Bulletin
 

class BulletinSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bulletin
        fields = ('id', 'smtp', 'port','username','password','tolist','cclist','bcclist',
        'btype','priority','state','color',
        'created_by','code','title','detail','effect','contact',
        'begin_time','end_time','duration',
        'ticket_case_url','ticket_case_id',
        'resolved_time','is_resolved','resolved_by','temporary_solution','permanent_solution','root_cause',
        'insert_time','modify_time','is_automated','is_deleted'
        )
