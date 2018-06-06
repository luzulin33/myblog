from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length = 40, blank=True)
    headshot = models.ImageField(upload_to = '%Y/%m/%d',default='default.jpg',blank=True,null=True,verbose_name='头像')
    signature = models.CharField(max_length=128, default='None')


    class Meta(AbstractUser.Meta):
        pass



