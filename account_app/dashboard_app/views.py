from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from account_app.dashboard_app import permissoins as _permissions
from django.contrib.auth import get_user_model
from account_app.dashboard_app.serializers import UserSerializer, PermissionSerializer
from django.contrib.auth.models import Group, Permission


@api_view(["GET"])
@permission_classes([_permissions.IsSuperUser])
def user_list(request):
    users = get_user_model().objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([_permissions.IsSuperUser])
def create_user(request):
    """
    {
        \n
        "password": "1234",
        "username": "ali5",
        "phone_number": "09147509740",
        "email": "alibehzad819@gmail.com"
    }

    """
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(
        data={"messages": ["متود ارسالی باید POST باشد"]},
        status=status.HTTP_400_BAD_REQUEST,
    )

@api_view(["GET"])
@permission_classes([_permissions.IsSuperUser])
def permissions(request):
    permission = Permission.objects.all()
    serializer = PermissionSerializer(permission, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
@permission_classes([_permissions.IsSuperUser])
def update_user_detail(request):
    pass
