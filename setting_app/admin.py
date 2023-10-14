from django.contrib import admin
from setting_app.models import Setting, Social, ContactUs, AboutUs

# Register your models here.

class SocialInline(admin.TabularInline):
    model = Social

class AboutUsInline(admin.TabularInline):
    model = AboutUs
    extra = 1


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('site_name',)
    inlines = [SocialInline, AboutUsInline]

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'is_read', 'date_send')
    list_editable = ('is_read',)
    list_filter = ('is_read', 'date_send')
    search_fields = ('full_name', 'email', 'text', 'title')