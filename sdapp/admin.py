from django.contrib import admin
from .models import Category,Product,Relatedimage

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','slug','category_image','is_active')
    list_editable=('is_active','slug')
    list_filter=('title','is_active')
    prepopulated_fields={"slug":("title",)}

admin.site.register(Category,CategoryAdmin)

class RelatedimageAdmin(admin.StackedInline):
    model=Relatedimage

class ProductAdmin(admin.ModelAdmin):
    list_display=('title','slug','product_image','is_active')
    list_editable=('is_active','slug')
    list_filter=('title','is_active')
    prepopulated_fields={"slug":("title",)}
    inlines=[RelatedimageAdmin]

admin.site.register(Product,ProductAdmin)