from django.urls import path
from account_app.dashboard_app.views import (
    user_list,
    create_user,
    permissions,
)

urlpatterns = [
    path("users/", user_list, name="user-list"),
    path('users/create/', create_user, name="create-user"),
    path('permissions/', permissions, name='permission'),
]
