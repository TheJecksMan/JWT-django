from django.urls import path
from . import views

urlpatterns = [
    #urls /api/v2/auth
    path('auth/login', views.login_account, name='login'),
    path('auth/registration', views.regustration_account, name='registration'),
    path('orc', views.file_orc),
]
