from django.urls import include, path

from . import views

app_name = 'users'

urlpatterns = [
    path(
        'auth/registration/',
        views.UserCreateView.as_view(),
        name='registration',
    ),
    path(
        'auth/',
        include('django.contrib.auth.urls')
    ),
    path(
        'profile/edit/',
        views.UserProfileUpdateView.as_view(),
        name='edit_profile',
    ),
]
