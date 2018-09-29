from django.contrib import admin
from .models import Apitest,Apistep,Apis
from product.models import Product

# Register your models here.

class ApistepAdmin(admin.TabularInline):
    list_display =['apistep','apiname','apiurl','apiparamvalue','apimethod','apiresult','apistatus','create_time','id','apitest']
    model = Apistep
    extra= 1

class ApitestAdmin(admin.ModelAdmin):
    list_display = ['apitestname','apitester','apitestresult','create_time','id']
    inlines = [ApistepAdmin]

class ApisAdmin(admin.ModelAdmin):
    list_display = ['apiname','apimethod','apiresult','apistatus','create_time','id']

    # model = Product
    # extra= 1

# class ApissAdmin(admin.ModelAdmin):
#     list_display = ['apiname','apistatus','create_time','id','product']
#     # inlines = [ApisAdmin]

admin.site.register(Apitest,ApitestAdmin)
admin.site.register(Apis,ApisAdmin)
# admin.site.register(Apis)