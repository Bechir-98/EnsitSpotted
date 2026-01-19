from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('n8n/new-messages/', views.new_messages_for_n8n, name='new_messages_for_n8n'),
    path('n8n/mark-sent/<int:message_id>/', views.mark_message_sent, name='mark_message_sent'),
]

