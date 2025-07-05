from django.urls import path
from .import views

urlpatterns = [
    path('',views.login_page,name='login_page'),
    path('register_page/',views.register_page,name='register_page'),
    path('home/',views.home_page,name='home'),
    path('hlogout_page/',views.logout_page,name='logout_page'),
]
