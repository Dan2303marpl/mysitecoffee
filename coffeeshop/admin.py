from django.contrib import admin
from .models import Coffe_sort, ap_equip, dop_ap

class Coffe_sortSetting(admin.ModelAdmin):
    list_display = ('sort','type', 'count','cost')

class ap_equipSetting(admin.ModelAdmin):
    list_display = ('equipment','count','cost')

class dop_apSetting(admin.ModelAdmin):
    list_display = ('sirop','cost','count')


admin.site.register(Coffe_sort, Coffe_sortSetting)
admin.site.register(ap_equip, ap_equipSetting)
admin.site.register(dop_ap, dop_apSetting)

















# Register your models here.
