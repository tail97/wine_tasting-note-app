from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# from django.forms import ModelForm

class Wine(models.Model):
    name = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)
    link =models.CharField(max_length=200, primary_key=True)
    wine_info = models.CharField(max_length=200)
    alcohol = models.CharField(max_length=200)
    category = models.CharField(max_length = 100)
    cdate = models.DateTimeField(default=now)
    price = models.CharField(max_length=200)
    discount = models.CharField(max_length=200)
    capacity = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f'{self.name}-{self.alcohol}-{self.category}-{self.price}-{self.discount}-{self.cdate}'
    
class White_wine(models.Model):
    name = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)
    link =models.CharField(max_length=200, primary_key=True)
    wine_info = models.CharField(max_length=200)
    alcohol = models.CharField(max_length=200)
    category = models.CharField(max_length = 100)
    cdate = models.DateTimeField(default=now)
    price = models.CharField(max_length=200)
    discount = models.CharField(max_length=200)
    capacity = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f'{self.name}-{self.alcohol}-{self.category}-{self.price}-{self.discount}-{self.cdate}'
    
class Rose_Wine(models.Model):
    name = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)
    link =models.CharField(max_length=200, primary_key=True)
    wine_info = models.CharField(max_length=200)
    alcohol = models.CharField(max_length=200)
    category = models.CharField(max_length = 100)
    cdate = models.DateTimeField(default=now)
    price = models.CharField(max_length=200)
    discount = models.CharField(max_length=200)
    capacity = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f'{self.name}-{self.alcohol}-{self.category}-{self.price}-{self.discount}-{self.cdate}'
    

class Tastingnote(models.Model):
    title = models.CharField(max_length=30) #??????
    content = models.TextField() #??????
    created_at = models.DateTimeField(auto_now_add=True) #add ??? ?????? ??????
    updated_at = models.DateTimeField(auto_now=True) #update ??? ?????? ??????
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/',blank = True) #?????????
    file_upload = models.FileField(upload_to = 'blog/file/%Y/%m/%d/',blank = True ) #????????? ??????
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) #?????????