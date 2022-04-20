from django.shortcuts import render,redirect
from .models import sanpham
from danhmuc.models import danhmuc
# Create your views here.
def get_sanpham(request,id):
    sanpham_list= sanpham.objects.filter(danhmuc_id= id)
    danhmuc_name= danhmuc.objects.get(danhmuc_id=id)
    return render(request,'sanpham.html',{'sanpham_list':sanpham_list, 'danhmuc_name':danhmuc_name})

def get_sanphamForm(request):
    danhmuc_list = danhmuc.objects.filter();
    return render(request,'sanphamForm.html',{"danhmuc_list":danhmuc_list})

def add_employee(request):
    if request.method =='POST':
        danhmuc_id = request.POST['danhmuc']
        name = request.POST['name']
        price = request.POST['price']
        sl = request.POST['sl']
        image = request.FILES['image']

        danhmucc = danhmuc.objects.get(danhmuc_id=danhmuc_id)
        sanphamm = sanpham.objects.create(danhmuc_id =danhmucc,
                                            name= name,
                                            price=price,
                                            sl=sl,
                                            image=image )
        sanphamm.save()
        return redirect('/danhmuc/'+ str(danhmuc_id))
    else:    
        return render(request,'error.html')

