from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from institute.models import Contact
from institute.models import Registration
from institute.models import Details

#Create your views here.

# def index(request):
    # if request.method=='POST':
         # c_course=request.POST['c_course']
         # c_type=request.POST['c_type']
         # c_roll=request.POST['c_roll']
         # i_data=Details(c_course=c_course,c_type=c_type,c_roll=c_roll)
         # i_data.save()  
         # return render(request,'index.html')       

def index(request):
    if request.method=='GET':
         c_course = 'c_course' in request.GET
         c_type = 'c_type' in request.GET
         c_roll = 'c_roll' in request.GET
         i_data=Details(c_course=c_course,c_type=c_type,c_roll=c_roll)
         i_data.save()  
         return render(request,'index.html')

def about(request):
     return render(request,'about.html')

def course(request):
     return render(request,'course.html')

def gallery(request):
     return render(request,'gallery.html')

def onlineregistration(request):
    if request.method=='POST':
         course=request.POST['course']
         qualification=request.POST['qualification']
         name=request.POST['name']
         father_name=request.POST['father_name']
         gender=request.POST['gender']
         mother_name=request.POST['mother_name']
         date=request.POST['date']
         address=request.POST['address']
         status=request.POST['status']
         pin=request.POST['pin']
         category=request.POST['category']
         mail=request.POST['mail']
         phone=request.POST['phone']
         branch=request.POST['branch']
         photo=request.POST['photo']
         data=Registration(course=course,qualification=qualification,name=name,father_name=father_name,gender=gender,mother_name=mother_name,date=date,address=address,status=status,pin=pin,category=category,mail=mail,phone=phone,branch=branch,photo=photo)
         data.save()
         messages.success(request,"You have Registered Successfully")
         return redirect('onlineregistration')
    else:    
     return render(request,'onlineregistration.html')
     
def checkresult(request):
     return render(request,'checkresult.html')     
     
def checkstatus(request):
     return render(request,'checkstatus.html')   

def managementteam(request):
     return render(request,'managementteam.html')          

def branchlist(request):
     return render(request,'branchlist.html')          

def selectedstudent(request):
     return render(request,'selectedstudent.html')          
       
def contact(request):
    if request.method=='POST':
         contact_name=request.POST['contact_name']
         contact_email=request.POST['contact_email']
         contact_phone=request.POST['contact_phone']
         contact_subject=request.POST['contact_subject']
         contact_message=request.POST['contact_message']
         contact_data=Contact(contact_name=contact_name,contact_phone=contact_phone,contact_email=contact_email,contact_subject=contact_subject,contact_message=contact_message)
         contact_data.save()
         messages.success(request,"Send Contact Details Successfully")
         return redirect('contact')
    else:     
       return render(request,'contact.html')          

def listt(request):
     return render(request,'listt.html')     