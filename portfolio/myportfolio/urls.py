
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('about/insert/', views.about_insert, name='about_insert'),
    path('about/edit/<int:id>', views.about_edit, name='about_edit'),
    path('about/edited/', views.edited, name='edited'),
    path('about/delete/<int:id>', views.delete, name='delete'),
]