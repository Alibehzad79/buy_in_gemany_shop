from rest_framework import serializers
from product_app.models import Product, Gallery, Comment
import datetime


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        exclude = ("id",)


class CommentSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    answre = serializers.CharField(read_only=True, required=False)
    date_send = serializers.DateField(default=datetime.date.today())

    class Meta:
        model = Comment
        exclude = ("id", "status")
        # fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    galleries = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    get_absolute_url = serializers.URLField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_galleries(self, obj):
        return [GallerySerializer(s).data for s in obj.galleries.all()]

    def get_comments(self, obj):
        return [
            CommentSerializer(s).data
            for s in obj.comments.filter(status="accept").all()
        ]

    def get_tags(self, obj):
        return [{"name": tag.name, "slug": tag.slug} for tag in obj.tags.all()]

    def get_category(self, obj):
        return [{"name": obj.category.name, "slug": obj.category.slug}]
