from django.contrib import admin

# Register your models here.
from django.contrib import admin
from sanpham.models import sanpham
# Register your models here.
class sanphamAdmin(admin.ModelAdmin):
    list_display=("sanpham_id","danhmuc_id","name","image","sl","price")
    search_fields=['name']
    list_filter=("sanpham_id","danhmuc_id","name","image","sl","price")
admin.site.register(sanpham,sanphamAdmin) 
