from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core import validators


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password", "phone_number"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data["username"],
            email=validated_data["email"],
            phone_number=validated_data["phone_number"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserDetail(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username", "first_name", "last_name", "phone_number", "email")


class RestPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class ChangePasswordSerializer(serializers.Serializer):
    password1 = serializers.CharField(
        required=True,
        validators=[
            validators.MinLengthValidator(6, "طول کاراکتر باید حداقل 6 باشد"),
            validators.MaxLengthValidator(12, "طول کاراکتر باید حداکثر 12 باشد"),
        ],
        label="رمز عبور جدید",
        style={'input_type': 'password'},
    )
    password2 = serializers.CharField(
        required=True,
        validators=[
            validators.MinLengthValidator(6, "طول کاراکتر باید حداقل 6 باشد"),
            validators.MaxLengthValidator(12, "طول کاراکتر باید حداکثر 12 باشد"),
        ],
        label="تایید رمز عبور",
        style={'input_type': 'password'},
    )