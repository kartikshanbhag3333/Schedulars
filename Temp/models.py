from django.db import models
from django.template.defaultfilters import default
from test.test_imageop import MAX_LEN

# Create your models here.
class LoginData(models.Model):
    username=models.CharField(max_length=128)
    password=models.CharField(max_length=128)
    about=models.CharField(max_length=400)
    image_path=models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.username;


class To_Do_List(models.Model):
    username=models.CharField(max_length=40)
    task_id=models.IntegerField()
    task_name=models.CharField(max_length=400)
    task_time=models.CharField(max_length=40)
    task_in_time=models.CharField(max_length=100)
    task_expected_time=models.CharField(max_length=100)
    task_type=models.CharField(max_length=100)
    
    
    def __unicode__(self):
        return self.task_name