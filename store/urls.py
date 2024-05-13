from django.urls import path
from . import  views 

urlpatterns = [
    path('',views.newindexpage,name='newindexpage'),
    path('about/',views.about,name='about'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),




]