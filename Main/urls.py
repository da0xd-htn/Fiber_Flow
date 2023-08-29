from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('Home/',views.HomeView.as_view(),name='Home'),
    path('SignIn/',views.AuthenticationView.as_view(),name='SignIn'),
    path('About/',views.AboutView.as_view(),name='About'),
    path('logout/', views.logout_view, name='logout'),

]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
