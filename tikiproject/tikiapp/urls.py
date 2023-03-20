from idlelib.textview import view_file

from django.contrib import admin
from django.urls import path , include , re_path , register_converter
from . import views
from .converters import CodeConverter ,StringAndNumberPathConverter, IntPathConverter , StringPathConverter , DateConverter

register_converter(CodeConverter , 'code_type')
register_converter(StringAndNumberPathConverter , 'stringnumber_type')
register_converter(IntPathConverter , 'Int_type')
register_converter(StringPathConverter , 'string_type')
register_converter(DateConverter , 'date_type')

urlpatterns = [
    path('', views.index , name="index"),
    # path('welcome/<int:year>' , views.welcome , name="welcome"),
    path('welcome/<string_type:year>' , views.welcome , name="hello"),
    path('test/' , views.TestView.as_view() , name="ahihi")
    # path('admin/', admin.site.urls),

]
