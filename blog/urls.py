from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('',home,name='home'),
    path('menu/',menu,name='menu'),
    path('logpage/',logpage,name='logpage'),
    path('signup/',signup,name='signup'),
    path('login/',login,name='login'),
]
