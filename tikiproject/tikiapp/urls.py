
from idlelib.textview import view_file

from django.contrib import admin
from django.urls import path , include , re_path , register_converter
from . import views
from rest_framework import routers
from .converters import CodeConverter ,StringAndNumberPathConverter, IntPathConverter , StringPathConverter , DateConverter

register_converter(CodeConverter , 'code_type')
register_converter(StringAndNumberPathConverter , 'stringnumber_type')
register_converter(IntPathConverter , 'Int_type')
register_converter(StringPathConverter , 'string_type')
register_converter(DateConverter , 'date_type')

router = routers.DefaultRouter()
router.register('categories' , views.CategoryViewSet)

router.register('products' , views.ProductViewSet)

# router.register('accounts' , views.AccountViewSet)
router.register('brands' , views.BrandViewSet)
router.register('sellers' , views.SellerViewSet)
router.register('customers' , views.CustomerViewSet)
router.register('category-ramdom' , views.CategoryRamdomViewSet)





urlpatterns = [
    path('', include(router.urls)),

    # path('admin/', admin.site.urls),


]
