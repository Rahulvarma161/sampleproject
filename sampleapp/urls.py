from django.urls import path, include
from . import views,uploadexcel


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.category_form,name='category_form'),
    path('subcategoryajax/',views.subcategoryajax,name='subcategoryajax'),
    path('save/',views.category_form,name='category_forms'),
    path('excel/',uploadexcel.uploadfile,name='uploadfile'),
]