from django.contrib import admin
from .models import Account , Seller , Customer , Category , List_Categoies , Cart_item , Cart , Product , Product_detail , Option , Option_group , Order , Order_item , Payment , Evaluate
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id' , 'categoryname' , 'image']
    search_fields = ['categoryname']
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

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'base_price' , 'category_name' , 'categoryDetail' , 'seller']
    search_fields = ['name' , 'category_name' , 'categoryDetail__name']
admin.site.register(Product , ProductAdmin)

class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'price' , 'quantity' , 'salable_quantity','active' , 'product' , 'option']
    search_fields = ['name' , 'price' , 'quantity', 'product__name' , 'option__name']
admin.site.register(Product_detail , ProductDetailAdmin)

class SellerAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'phone' , 'address' , 'isOfficial' , 'isChecked' , 'account']
    search_fields = ['name' , 'phone' , 'address' ,'account__username' ]
    list_filter = ['isOfficial' , 'isChecked']
admin.site.register(Seller , SellerAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id' , 'fullname' , 'address' , 'gender' , 'DOB' , 'account']
    search_fields = ['fullname' , 'gender' , 'account__username']

admin.site.register(Customer , CustomerAdmin)

class AccountAdmin (admin.ModelAdmin):
    list_display = ['id' , 'username' , 'role']
    search_fields = ['username']
admin.site.register(Account , AccountAdmin)








