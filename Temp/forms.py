'''
Created on Mar 6, 2015

@author: kartiksahnbhag
'''
from Temp.models import LoginData,To_Do_List;
from django import forms

class LoginForm(forms.ModelForm):
    username=forms.CharField(max_length=128);
    password=forms.CharField(max_length=128);
    about=forms.CharField(max_length=400)
    image_path=forms.CharField(max_length=100)
    class Meta:
        model=LoginData;
        
class To_Do_List(forms.ModelForm):
    task_name=forms.CharField(max_length=400)
    task_time=forms.CharField(max_length=40)
    task_id=forms.IntegerField()
    task_in_time=forms.CharField(max_length=100)
    task_expected_time=forms.CharField(max_length=100)
    task_para=forms.CharField(max_length=100)
    class Meta:
        model=To_Do_List;
    fields = ('task_name', 'task_time','task-id','task_in_time','task_expected_time','task_para')