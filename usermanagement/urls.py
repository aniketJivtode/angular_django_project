
from django.urls import path
from usermanagement.views import RegisterView, LoginView,UserProfileList,UserProfileDetail,_logout
# from .tokens import CustomTokenObtainPairView, _login, _logout
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [

    path('login/', LoginView.as_view(), name='login'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),

    path('profiles/', UserProfileList.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', UserProfileDetail.as_view(), name='profile-detail'),
]