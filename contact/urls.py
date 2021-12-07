from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.allContact),
    path('contact/<int:id>/', views.getById),
    path('add/', views.addContact),
    path('updateContact/<int:id>/', views.updateContact),
    path('deleteContact/<int:id>/', views.deleteContact)
  
]
