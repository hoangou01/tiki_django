

from django.contrib import admin
from django.utils.html import mark_safe
from django.contrib.auth.models import Permission
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Account , Category ,  Cart_item , Cart , Product,  Order , Order_item , Payment , Evaluate
# Register your models here.

# admin.site.register(Permission)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id' , 'categoryname' , 'image_tag']
    search_fields = ['categoryname']
    # readonly_fields = ['image']
    def image(self , category):
        return mark_safe(
                "<img src='/static/{img_url}' />".format(img_url=category.image.name))
admin.site.register(Category ,CategoryAdmin)


class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    class meta:
        model = Product
        fields = '__all__'

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ['id' , 'name' , 'quantity' , 'salable_quantity', 'base_price' ,'description' , 'category' , 'seller' , 'is_active']
    search_fields = ['name' , 'category__categoryname' , 'description']
    list_filter = ['is_active']
admin.site.register(Product , ProductAdmin)

class AccountAdmin (admin.ModelAdmin):
    list_display = ['id' , 'username' , 'is_seller' , 'is_customer' , 'is_superuser']
    search_fields = ['username']
admin.site.register(Account , AccountAdmin)








