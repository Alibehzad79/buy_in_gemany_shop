from django.contrib import admin
from slider_app.models import Slider

# Register your models here.


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ("title", "active")
    list_editable = ("active",)
    list_filter = ("active",)
    search_fields = ("title", "content", "url")
