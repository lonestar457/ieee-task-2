from django.urls import path 
from . import views

urlpatterns= [
    path ('ticket_details/<int:pk>/',views.ticket_details, name= 'ticket_details'),
    path ('create_ticket/',views.create_ticket, name= 'create_ticket'),
    path ('all_tickets/',views.all_tickets, name= 'all_tickets'),
    path ('ticket_queue/',views.ticket_queue, name= 'ticket_queue'),
    path ('accept_ticket/<int:pk>/',views.accept_ticket, name= 'accept_ticket'),
    path ('close_ticket/<int:pk>/',views.close_ticket, name= 'close_ticket'),
    path ('workspace/',views.workspace, name= 'workspace'),
    path ('update_ticket/<int:pk>/',views.update_ticket, name= 'update_ticket')]