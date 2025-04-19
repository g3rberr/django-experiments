from django.urls import path
from django.contrib.auth.views import LoginView

from .views import (
    get_cookie_view,
    set_cookie_view,
    set_session_view,
    get_session_view,
    MyLogoutView,
    AboutMeView,
    RegisterView
)


app_name = 'myauth'

urlpatterns = [
    # path('', login_view, name='login'),
    path(
        'login/',
        LoginView.as_view(
            template_name='myauth/login.html',
            redirect_authenticated_user=True, # сразу редиректит аутентифицированных пользователей
            ), 
            name='login'
    ),
    path('logout/', MyLogoutView.as_view(), name='logoout'),
    path('about-me/', AboutMeView.as_view(), name='about-me'),
    path('register/', RegisterView.as_view(), name='register'),

    path('cookie/get/', get_cookie_view, name='cooke-get'),
    path('cookie/set/', set_cookie_view, name='cooke-set'),

    path('session/set/', set_session_view, name='session-set'),
    path('session/get/', get_session_view, name='session-get'),
]