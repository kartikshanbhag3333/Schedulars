from django.http import HttpResponse;
from django.shortcuts import render_to_response;
from django.template.context import RequestContext
from Temp.models import LoginData, To_Do_List
from Temp.forms import LoginForm
from django.contrib.admin import models
from django.http.response import HttpResponseRedirect, HttpResponseRedirectBase
import Temp
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import math;
import datetime;
from datetime import date,time,datetime,timedelta;
from django.contrib.auth.views import logout as original_logout
# Create your views here.
def deletetask(request):
    ids= request.POST['delete'];
    ids=ids.split('$');
    for id in ids:
        print id;
        instance=To_Do_List.objects.filter(id=int(id))
        print instance
        instance.delete();
    
    
    
    return HttpResponse("OK");
def logout(request):
    for sesskey in request.session.keys():
        del request.session[sesskey]
    return HttpResponse("OK")

def error(request):
    return render_to_response("temp/Error.html")

def getLastCount(request):
    count=request.POST['count']
    username=request.session['username']
    users=LoginData.objects.filter(username=username);
    for user in users:
        user_id=user.id
    tasks=To_Do_List.objects.filter(username=user_id).order_by("-task_expected_time")[int(count):(int(count)+10)]
    context=request.getcontext();
    if(request.POST['newtask']=="true"):
        context_dict={'tasks': tasks}
    else:
        context_dict={};
    return HttpResponse(str(tasks.count()),context_dict,context);

def gettask(request):
    username=request.session['username']
    print username  
    user_data=LoginData.objects.filter(username=username)
    for a in user_data:
        user_id=a.id;
    data_req=request.POST['data']
    print data_req
    tasks=To_Do_List.objects.filter(username=user_id).order_by("-task_expected_time").reverse()[int(data_req):(int(data_req)+10)]
    return_string=''
    for task in tasks:
        return_string+='<li><span class="handle ui-sortable-handle">\n<i class="fa fa-ellipsis-v"></i>\n<i class="fa fa-ellipsis-v"></i>\n</span>\n'
        return_string+='<input type="radio">\n'
        return_string+='<span class="text" id="check">'+task.task_name+'</span>\n'
        return_string+='<small class="label label-danger"><i class="fa fa-clock-o"></i>'+task.task_time+'</small>\n'
        return_string+='<div class="tools">\n<i class="fa fa-edit"></i>\n<i class="fa fa-trash-o"></i>\n</div></li>'
    return_string+=''
        
    return HttpResponse(return_string);

def addtask(request):
    try:
        if not request.session.get('form-submitted', False):
            return HttpResponse("Session Expired")
        else:
            #logic to add the task to database
            x=datetime.now()
            task_name=request.POST['taskname'];
            print "here"
            task_time=request.POST['tasktime'];
            print "here"
            task_para=request.POST['timepara'];
            print "here"
            print "The task parama is  :  " + task_name+"/"+task_time+"/"+task_para;
            user=LoginData.objects.filter(username=request.session['username'])
            for a in user:
                user_id=a.id;
            counts=To_Do_List.objects.filter(username=str(user_id)).count();
            print "The Count is : " + str(counts);
            temp=str(user_id)+str(counts)
            print temp
            task_id=int(temp)
            print task_id
            #print "The Task Tiem is : " + task_id
            time_scheduled=datetime.combine(date.today(),time(x.hour,x.minute,x.second))
            if(task_para=="Minutes"):
                time_expected=time_scheduled+timedelta(minutes=int(task_time))
            elif(task_para=="Hours"):
                time_expected=time_scheduled+timedelta(hours=int(task_time))
            elif(task_para=="Days"):
                time_expected=time_scheduled+timedelta(days=int(task_time))
            else:
                time_expected=time_scheduled+timedelta(weeks=int(task_time))
            task_time=task_time+" "+task_para 
            print task_time
            task_type=request.POST['tasktype']  
            print task_type
            task=To_Do_List(username=user_id,task_id=task_id,task_name=task_name,task_time=task_time,task_in_time=time_scheduled,task_expected_time=time_expected,task_type=task_type)
            task.save()
            return HttpResponse("Task Scheduled Successfully")
            
        
    except:
        return HttpResponse("Error Adding your task")

def schedule(request):
    context=RequestContext(request);
    if not request.session.get('form-submitted', False):
        return redirect("Temp.views.index")
    else:
        #request.session['form-submitted']=False
        username=request.session['username'];
        data=LoginData.objects.filter(username=username);
        for x in data:
            id=x.id;
            about=x.about;
            filename=x.image_path;
        print about;
        about=about.split('/');
        tasks=To_Do_List.objects.filter(username=id).order_by("-task_expected_time").reverse()
        to_do_count=tasks.count();
        print str(to_do_count)
        if to_do_count!=0:
            if(to_do_count%10!=0):
                f=int(round((to_do_count/10)+0.5))
            else:
                f=int(to_do_count/10)
        else:
            f=0
        print str(f)
        #to_do_count=1
        
        print tasks;
        print "The Count is : " + str(f)
        #f=20
        return render_to_response("temp/mainScreen.html",{'username':username,'about1':about[0],'about2':about[1],'filename':filename,'id':id,'count':range(f),'range':f,'tasks':tasks[0:10]}  ,context)
def index(request):
    context=RequestContext(request)
    context_dict={};
    return render_to_response("temp/index.html",context_dict,context);

def login(request):
    context=RequestContext(request)
    if request.method == 'POST':
        form=LoginForm(request.POST)
        print "hello"
        print request.POST;
        username=request.POST['username']
        password=request.POST['password']
        context_dict={'username': username};
        print username;
        print password;
        count=LoginData.objects.filter(username=username,password=password).count();
        if count == 0:
            return HttpResponse("Invalid Login Credentials");
        else:
            request.session['form-submitted'] = True;
            request.session['username']=username
            data=LoginData.objects.filter(username=username,password=password);
            #request.session['about']=data.about;
            #request.session['image']=data.image_path;
            request.session.set_expiry(400)
            return HttpResponse("OK")
            #return redirect('ultron.views.schedule')
            #return render_to_response("ultron/mainScreen.html",context_dict,context)
                        
