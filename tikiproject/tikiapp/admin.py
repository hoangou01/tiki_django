

from django.contrib import admin
from django.utils.html import mark_safe
from django.contrib.auth.models import Permission
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Account , Seller , Customer , Category , List_Categoies , Cart_item , Cart , Product , Product_detail , Option , Option_group , Order , Order_item , Payment , Evaluate
# Register your models here.

# admin.site.register(Permission)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id' , 'categoryname' , 'image_tag']
    search_fields = ['categoryname']
    # readonly_fields = ['image']
    # def image(self):
    #     return mark_safe(
    #             "<img src='/static/{img_url}' />".format(img_url=self.image.url))
admin.site.register(Category ,CategoryAdmin)
class Option_groupAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name']
    search_fields = ['name']
admin.site.register(Option_group , Option_groupAdmin)

class OptionAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name','option_group']
    search_fields = ['name']
admin.site.register(Option , OptionAdmin)

class List_CategoryAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'category']
admin.site.register(List_Categoies , List_CategoryAdmin)

class ProductForm(forms.ModelForm):
    class meta:
        model = Product
        fields = '__all__'

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ['id' , 'name' , 'base_price' , 'category_name' , 'categoryDetail' , 'seller']
    search_fields = ['name' , 'category_name' , 'categoryDetail__name']
admin.site.register(Product , ProductAdmin)

class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'price' , 'quantity' , 'salable_quantity','active' , 'product' , 'option']
    search_fields = ['name' , 'price' , 'quantity', 'product__name' , 'option__name']
admin.site.register(Product_detail , ProductDetailAdmin)

class SellerForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    class meta:
        model = Seller
        fields = '__all__'
class SellerAdmin(admin.ModelAdmin):
    form = SellerForm
    list_display = ['id' , 'name' , 'phone' , 'address' , 'isOfficial' , 'is_active' , 'account']
    search_fields = ['name' , 'phone' , 'address' ,'account__username' ]
    list_filter = ['isOfficial' , 'is_active']
admin.site.register(Seller , SellerAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id' , 'fullname' , 'address' , 'gender' , 'DOB' , 'account']
    search_fields = ['fullname' , 'gender' , 'account__username']

admin.site.register(Customer , CustomerAdmin)

class AccountAdmin (admin.ModelAdmin):
    list_display = ['id' , 'username' , 'is_seller' , 'is_customer' , 'is_superuser']
    search_fields = ['username']
admin.site.register(Account , AccountAdmin)








