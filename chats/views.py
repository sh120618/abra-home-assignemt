from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, ListAPIView
from .models import Message
from .serializers import MessageSerializer, CreateMessageSerializer


'''
    # message class to view messages for each user as a sender or receiver
    # HTTP mrthods allow: GET, POST, DELETE
    # must login to view messages.
    
'''


class MessageViewSet(ListCreateAPIView, RetrieveDestroyAPIView, GenericViewSet):

    permission_classes = [IsAuthenticated]

    # custom serializer depend on HTTP request

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateMessageSerializer
        return MessageSerializer

    # queryset for getting logged in user as a sender or receiver
    def get_queryset(self):
        user = self.request.user
        queryset = Message.objects.filter(
            Q(receiver=user.id) | Q(sender=user.id))
        return queryset

    # updating 'is_read' field after mapping to message-detail
    def retrieve(self, request, *args, **kwargs):
        user = self.request.user
        message = get_object_or_404(Message, pk=kwargs['pk'])
        if message.receiver.id == user.id:
            message.is_read = True
            message.save()
        return super().retrieve(request, *args, **kwargs)


'''
    # view for unread messages of the logged in user
'''


class MessageUnread(ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    # queryset returns filter message object sent to the user and didnt read
    def get_queryset(self):
        user = self.request.user.id
        queryset = Message.objects.filter(receiver=user, is_read=False)
        return queryset
