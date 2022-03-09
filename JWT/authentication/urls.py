from django.urls import path
from . import views

urlpatterns = [
    #urls /api/auth
    path('auth/registration', views.sing_up),
    path('auth/login', views.sing_in),
    path('edit/edit_profile', views.edit_profile),
    path('logout', views.logout_user),
]
