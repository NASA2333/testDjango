from django.contrib import admin
from .models import Apitest,Apistep

# Register your models here.

class ApistepAdmin(admin.TabularInline):
    list_display =['apistep','apiname','apiurl','apiparamvalue','apimethod','apiresult','apistatus','create_time','id','apitest']
    model = Apistep
    extra= 1

class ApitestAdmin(admin.ModelAdmin):
    list_display = ['apitestname','apitester','apitestresult','create_time','id']
    inlines = [ApistepAdmin]

admin.site.register(Apitest,ApitestAdmin)