from email.policy import default
from pickle import NONE

from danhmuc.models import danhmuc
from django.db import models
from danhmuc.models import danhmuc
# Create your models here.
class sanpham(models.Model):
    sanpham_id= models.AutoField(primary_key=True)
    danhmuc_id= models.ForeignKey(danhmuc,default=None, on_delete=models.CASCADE)
    name=models.CharField(max_length=30,null=False)
    sl = models.IntegerField(null=True)
    image = models.ImageField(upload_to='images',null=False,default=None)
    price =models.CharField(max_length=20,null=False)

    def __str__(self) :
        return f"{self.sanpham_id},{self.danhmuc_id},{self.name},{self.sl},{self.image},{self.price}"

