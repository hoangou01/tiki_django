from django.contrib import admin
from .models import Account , Seller , Customer , Category , List_Categoies , Cart_item , Cart , Product , Product_detail , Option , Option_group , Order , Order_item , Payment , Evaluate
# Register your models here.
admin.site.register(Category)
admin.site.register(List_Categoies)
admin.site.register(Product)
admin.site.register(Product_detail)
admin.site.register(Option)
admin.site.register(Option_group)
admin.site.register(Seller)
admin.site.register(Customer)
