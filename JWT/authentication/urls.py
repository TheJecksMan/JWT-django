from django.urls import path
from . import views

urlpatterns = [
    #urls /api/auth
    # path('registration/', views.RegistrationAPI.as_view(), name='reg'),
    path('login/', views.sing_up),
    # path('logout/', views.RegistrationAPI.as_view(), name='logout'),
    # path('test-api/', views.TestAPI.as_view(), name='test'),
    path('test/', views.test_token),
]
