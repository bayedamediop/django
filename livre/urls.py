from django.urls import path
from . import views

urlpatterns = [
    path('books/',views.allBooks),
    path('book/<int:id>/', views.getById),
    path('addBooks/', views.addBook),
    path('update/<int:id>/', views.updateBook),
    path('delete/<int:id>/', views.deleteBook)
  
]
