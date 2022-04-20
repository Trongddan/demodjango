from django.shortcuts import render
from .models import danhmuc
# Create your views here.
def get_home(request):
    danhmuc_list= danhmuc.objects.filter().order_by("danhmuc_id")
    return render(request,"home.html",{'danhmuc_list':danhmuc_list})