from django.urls import path
from . import views as baseViews
from .news import views as newsViews

urlpatterns = [
    #urls /api/v2/auth
    path('auth/login', baseViews.login_account, name='login'),
    path('auth/registration', baseViews.regustration_account, name='registration'),
    path('orc', baseViews.file_orc),
    path('news', newsViews.list_news)
]
