from django.urls import path
from . import views
from .views import signup_view, login_view


urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.home, name='index'),

    path('menu/', views.menu, name='menu'),
    path('my-order/', views.my_order, name='my_order'),
    path('place-order/<int:item_id>/', views.place_order, name='place_order'),

    path('about/', views.about, name='about'),

    # AUTH
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

   
  

