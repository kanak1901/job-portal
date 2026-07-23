from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('employer/register/', views.employer_register, name='employer_register'),
    path('login/', views.user_login, name='login'),
    path('employer/login/', views.employer_login, name='employer_login'),
    path('logout/', views.user_logout, name='logout'),
]
