from django.urls import path
from account_app.views import register_user, user_detail, get_reset_password
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register/', register_user, name="user-register"),
    path('user/', user_detail, name="user-detail"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('reset-password/', get_reset_password, name='reset-password'),
]
