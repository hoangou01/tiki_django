
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
# router.register('listcategories' , views.ListCategoryViewSet)
router.register('accounts' , views.AccountViewSet)
router.register('signup/sellers' , views.sellerViewSet)
router.register('signup/customer' , views.customerViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('signup/sellers', views.sellerViewSet.as_view({'post'})),

    # path('admin/', admin.site.urls),


]
