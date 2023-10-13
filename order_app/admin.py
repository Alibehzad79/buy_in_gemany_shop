from django.contrib import admin
from order_app.models import Order, PaidOrder, BankPay

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'paid_price', 'is_paid', 'date_created', 'full_price')
    list_filter = ('is_paid', 'date_created')
    list_editable = ('is_paid',)
    search_fields = ('user', 'product')
    
@admin.register(PaidOrder)
class PaidOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'pay', 'complete', 'status', 'date_created')
    list_filter = ('status', 'date_created', 'complete')
    list_editable = ('status', 'complete')
    search_fields = ('user', 'product')

@admin.register(BankPay)
class BankPayAdmin(admin.ModelAdmin):
    list_display = ('user', 'order', 'code', 'card_pan', 'date_created')
    list_filter = ('date_created',)
    search_fields = ('user', 'order', 'card_pan', "ref_id", "card_hash")
