from django.contrib import admin
from django.urls import path , include
from .views import *
from django.conf.urls.static import static
from django.conf import settings

 
urlpatterns = [
    path('',product_view, name= 'product_view'),
    path('signup', handleSignUp, name="handleSignUp"),
    path('login', handleLogin, name="handleLogin"),
    path('logout', handleLogout, name="handleLogout"),
    path('contact', contact, name="contact")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)