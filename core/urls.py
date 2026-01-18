from django.urls import path
from . import views,new_messages_for_n8n, mark_message_sent

urlpatterns = [
    path('', views.home, name='home'),
    path("api/n8n/messages/", new_messages_for_n8n),
    path("api/n8n/messages/<int:msg_id>/sent/", mark_message_sent),
]
