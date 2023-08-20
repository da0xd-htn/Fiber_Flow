from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='Home'),
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
