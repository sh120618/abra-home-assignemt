
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.MessageViewSet, basename='messages')


urlpatterns = [
    path('unread/', views.MessageUnread.as_view()),
    path('', include(router.urls)),
]
