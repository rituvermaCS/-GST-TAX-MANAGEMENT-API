from knox import views as knox_views
from .views import LoginAPI, RegisterAPI, UserAPI, UpdateProfileView, userDelete, userList, UserDetail 
from django.urls import path
from . import views

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/user/', UserAPI.as_view(), name='user'),
    path('api/updateprofile/<int:pk>/', UpdateProfileView.as_view(), name='changeProfile'),
    path('api/delete/<int:pk>/', views.userDelete, name="profile-delete"),
    path('api/list/', views.userList, name="list"),
    path('api/detail/', UserDetail.as_view(), name="detail"),
]
