from django.urls import path
from . import views
 
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('delete/<username>/', views.DeleteView.as_view(), name='delete'),
    path('get_users/', views.GetView.as_view(), name='get'),
    path('data/', views.Get_ProductsView.as_view(), name='data'),
]