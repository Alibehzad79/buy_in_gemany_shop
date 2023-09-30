from django.contrib import admin
from product_app.models import Product, Category, Tag, Gallery, Comment

# Register your models here.
class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 4



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'price', 'category', 'status')
    list_editable = ('status',)
    search_fields = ('title', 'slug', 'content')
    list_filter = ('category__name', 'tags')
    inlines = [
        GalleryInline
    ]
    
admin.site.register(Category)    
admin.site.register(Tag)    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_send', 'status')
    list_filter = ('status',)
    list_editable = ('status',)
    search_fields = ('name', 'email', 'text', 'answre')