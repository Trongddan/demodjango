from django.db import models
# Create your models here.
class danhmuc(models.Model):
    danhmuc_id= models.AutoField(primary_key=True)
    name =models.CharField(max_length=20,null=False)
    
    def __str__(self):
        return f"{self.danhmuc_id},{self.name}"
