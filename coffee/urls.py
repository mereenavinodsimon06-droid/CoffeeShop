from django.urls import path
from . import views
from .views import signup_view, login_view

urlpatterns = [
    path('', views.home, name='index'),        
    path('menu/', views.menu, name='menu'),
    path('order/', views.my_order, name='my_order'),
    path('order/<int:item_id>/', views.place_order, name='place_order'),
    path('about/', views.about, name='about'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),

   
  
]
