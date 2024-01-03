
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('about/insert/', views.about_insert, name='about_insert')
]