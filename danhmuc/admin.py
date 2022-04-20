from django.contrib import admin
from danhmuc.models import danhmuc
# Register your models here.
class danhmucAdmin(admin.ModelAdmin):
    list_display=("danhmuc_id","name")
    search_fields=['name']
    list_filter=("danhmuc_id","name")
admin.site.register(danhmuc,danhmucAdmin) 
