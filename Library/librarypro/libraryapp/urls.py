from django.urls import path
from . import views
urlpatterns = [
    path('', views.book_list, name='home'), 
    path('create/', views.create_book, name='create_book'),
    path('list/', views.book_list, name='book_list'),
    path('update/<pk>/', views.update_book, name='update_book'),
    path('delete/<pk>/', views.delete_book, name='delete_book'),
    

]

