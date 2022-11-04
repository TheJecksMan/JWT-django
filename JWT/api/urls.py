from django.urls import path
from . import views as baseViews
from .news import views as newsViews

urlpatterns = [
    #urls /api/v2/auth
    path('profile/current', baseViews.current_account, name='current'),
    path('auth/logout', baseViews.logout_account, name='logout'),
    path('auth/login_site', baseViews.login_account_site, name='login_site'),
    path('auth/login', baseViews.login_account, name='login_mobile'),
    path('auth/registration', baseViews.regustration_account, name='registration'),
    path('orc', baseViews.file_orc),
    path('news', newsViews.ListNews.as_view()),
    path('post', newsViews.Post.as_view())
]
