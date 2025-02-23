from .models import Messages
from rest_framework import serializers


class MessagesSerializer(serializers.HyperlinkedModelSerializer):
    sender = serializers.CharField(source="sender_id")
    receiver = serializers.CharField(source="receiver_id")

    class Meta:
        model = Messages
        fields = '__all__'
