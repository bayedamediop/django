from django.conf.urls import url
from rest_framework import views
from django.urls import path
from . import views

from .views import FileView

urlpatterns = [
    url('upload/', FileView.as_view(), name='file-upload'),
    url('getFile/', views.getfile),
    path('getbyid/<int:id>/', views.getById),
    path('updateFile/<int:id>/', views.updateFille),
    path('deleteFile/<int:id>/', views.deleteFile)
]