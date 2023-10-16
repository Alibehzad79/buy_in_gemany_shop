from rest_framework import serializers
from setting_app.models import Setting, Social, AboutUs, ContactUs


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        exclude = ("is_read",)

    def create(self, validate_data):
        _contactus = ContactUs(
            full_name=validate_data["full_name"],
            email=validate_data["email"],
            title=validate_data["title"],
            text=validate_data["text"],
            date_send=validate_data["date_send"],
        )
        _contactus.save()
        return _contactus


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = "__all__"


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"


class SettingSerializer(serializers.ModelSerializer):
    socials = serializers.SerializerMethodField()
    aboutus = serializers.SerializerMethodField()

    class Meta:
        model = Setting
        fields = "__all__"

    def get_socials(self, obj):
        return (SocialSerializer(s).data for s in obj.socials.all())

    def get_aboutus(self, obj):
        return (AboutUsSerializer(s).data for s in obj.aboutus.all())
