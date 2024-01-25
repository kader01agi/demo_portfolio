
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('registrationConfirm/', views.registrationConfirm, name='registrationConfirm'),
    path('about/insert/', views.about_insert, name='about_insert'),
    path('email_verification/<str:id>', views.email_verification, name='email_verification'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('loginAdmin/', views.loginAdmin, name='loginAdmin'),
    path('about/edit/<int:id>', views.about_edit, name='about_edit'),
    path('about/edited/', views.edited, name='edited'),
    path('about/delete/<int:id>', views.delete, name='delete'),
]