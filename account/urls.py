from .views import RegisterAPI
from knox import views as knox_views
from .views import LoginAPI
from .views import RegisterAPI, follow, my_followers, my_following
from .views import ChangePasswordView
from django.urls import path

urlpatterns = [
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('follow/<int:follow_id>/', follow, name = 'follow'),
    path('my_followers/', my_followers, name = 'my_followers'),
    path('my_following/', my_following, name = 'my_following'),
]