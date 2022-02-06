from django.urls import path
from . import views

urlpatterns = [
    #urls /api/auth
    path('registration/', views.sing_up),
    path('generate_token', views.generations_tokens),
]
