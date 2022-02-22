from django.urls import path
from . import views

urlpatterns = [
    #urls /api/auth
    path('registration/', views.sing_up),
    path('login/', views.sing_in),
    path('generate_token', views.generations_tokens),
]
