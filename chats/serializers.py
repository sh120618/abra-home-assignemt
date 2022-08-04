from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from .models import Message



# serialzier for creating user object
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password',
                  'email', 'first_name', 'last_name']

# serialzier for creating message object
class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['subject', 'content', 'receiver']

# serialzier for message object
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        id = serializers.IntegerField(read_only=True)
        model = Message
        fields = ['id', 'subject', 'content', 'sender', 'receiver']
