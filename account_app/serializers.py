from rest_framework import serializers
from django.contrib.auth import get_user_model


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
    
    # def clean_email(self):
    #     email = self.data['email']
    #     print(email)
    #     if get_user_model().objects.get(email=email).exists():
    #         return email
    #     return serializers.ValidationError("کاربری با این ایمیل یافت نشد.")