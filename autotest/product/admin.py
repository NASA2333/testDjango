from django.contrib import admin
from .models import Product
from apitest.models import Apitest,Apis

# Register your models here.

#不明白这样做的意思在哪，暂时隐藏，未发现有啥影响
# class ApisAdmin(admin.TabularInline):
#     list_display = ['apiname','apiurl','apiparamvalue','apimethod','apiresult','apistatus','create_time','id','product']
#     inlines =['apiname','apiresult','apistatus','create_time','id']
#     # model = Apis
#     # extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname','productdesc','producter','create_time','id']
    # inlines = [ApisAdmin]




admin.site.register(Product,ProductAdmin)