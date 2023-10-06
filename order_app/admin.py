from django.contrib import admin
from order_app.models import Order, OrderItem

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'paid_price', 'is_paid', 'date_created', 'full_price')
    list_filter = ('is_paid', 'date_created')
    list_editable = ('is_paid',)
    search_fields = ('user',)
    inlines = [OrderItemInline]