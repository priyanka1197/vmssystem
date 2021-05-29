from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from accounts.models import guest , Host
from accounts.forms import *
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from accounts.authenticationbackend import AuthenticationBackend 
import random

def home(request):
    return render(request, 'homepage.html')

## manager details for visitors
def doctors(request):
    hosts = Host.objects.all()
    parameters = {'hosts':hosts}
    return render(request,'doctors.html',parameters)

## Login page for admin
def loginPage(request):
    if request.method== 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        
        user = auth.authenticate(username=username1,password=password1)
        print(user)
        #import pdb ; pdb.set_trace()
        if user is not None:
            auth.login(request, user)
            return redirect("/dashboard")
        else:
            return redirect('/admin_login/')

    else:
        return render(request,'admin_login.html')
        
def manager_login(request):
   if request.method == 'POST':
        #import pdb ; pdb.set_trace()
        username = request.POST.get('username')
        password = request.POST.get('password')
        authobject = AuthenticationBackend()

        user = authobject.authenticate(username=username, password=password)
        #import pdb ; pdb.set_trace()
        if user is not None: 
                host=authobject.get_user(username)
                print(host)
                return render(request,"managdashboard.html",{'host':host})

        else:
                return redirect("/manager_login")
   else:
                return render(request,"login.html")
	


def guestdetail(request):
     if request.POST.get("guest"):    
            host_id = request.POST.get("guest")
            host = Host.objects.get(id = host_id)
            form = Visitorform()
            param = {'form':form,'host':host}
            return render(request, 'guestdetail.html', param)
@csrf_exempt
def save_guest(request):
   if request.method == 'POST':
        hostname = request.POST.get('host')
        host = Host.objects.get(host_name=hostname)
        form = Visitorform(request.POST,request.FILES)
        for field in form:
            print("Field Error:", field.name,  field.errors)
        #import pdb ; pdb.set_trace()
        if form.is_valid():
            instance = form.save(commit=False)
            instance.hostname = hostname
            instance.save()
            rec = [host.host_email]
            subject = instance.name +" Checked In !"
            guest = instance
            ## EMAIL AND SMS TO HOST
            email(subject,guest,rec)
            messages.success(request,'Information sent to Host, You will be contacted shortly !!')
            return redirect('/doctors')
        else:
            pass
   else:
        return redirect('/doctors')
def email(subject,guest,rec,host=None):
    ## FILL IN YOUR DETAILS HERE
    sender = 'raspiinvent@gmail.com'
    html_content = render_to_string('hmail.html', {'guest':guest}) # render with dynamic value
    text_content = strip_tags(html_content)

    # try except block to avoid wesite crashing due to email error
    try:
        msg = EmailMultiAlternatives(subject, text_content, sender, rec)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    except:
        pass
    return

@csrf_exempt
def checkin(request): 
    mid = request.GET.get("mid")  
    form = time()
    param = {'form':form,'mid':mid}
    return render(request, 'checkin.html', param)
@csrf_exempt


def checkinsubmit(request):     
     if request.method == 'POST':
         form = time(request.POST)
         #import pdb;pdb.set_trace()
         if form.is_valid():
           timeassign = form.cleaned_data['timeassigned'] 
           mid = form.cleaned_data['mid']
           Guest = guest.objects.get(id=mid) 
           otp = random.randint(1000,9999)
           Guest.otp = otp      
           Guest.save() 
           message = "Your Meeting confirmed with "+Guest.hostname+". is at "+timeassign+". Your otp is"+str(otp)
           recipients = [Guest.email]
           subject = "Visitors meeting confirmation"
           sender = 'Priyanka4.p.cp@gmail.com'
           send_mail(subject, message, sender, recipients)
           print("mail send")
           message = SmsMessage(body='"Your Meeting confirmed with "+Guest.hostname+". is at "+timeassign+". Your otp is"+str(otp)',from_phone='+918378991811', to=['Guest.phoneno'])
           message.send()
           print("SMS send")
           return render(request, 'doctors.html')
@csrf_exempt
def company(request):
   if request.method == 'POST':
        otp = request.POST.get("otp")  
        #import pdb ; pdb.set_trace()
        Guest = guest.objects.get(otp=otp)
        if Guest is not None:
             host = Host.objects.get(host_name=Guest.hostname)
             Guest.otp = "null"
             Guest.save()
             form = Meeting_form()
             param = {'form':form,'host':host,'Guest':Guest}
             return render(request, 'meeting_form.html', param)	
        else:
             messages.success(request,'Please Enter Correct OTP')
             return render(request, 'company.html')

   else:
        return render(request, 'company.html')

def managerguest(request):
    if request.method == 'POST':
         if request.POST.get("host"): 
                 guest_name = request.POST.get('host')
                 visitor = list(guest.objects.filter(hostname=guest_name))
                 info = {'visitor':visitor}
                 return render(request,'visitor.html',info)
def guestinfo(request):
    if request.method == 'POST':
         if request.POST.get("guest"): 
                 guest_name = request.POST.get('guest')
                 visitor = guest.objects.get(id=guest_name)
                 info = {'visitor':visitor}
                 return render(request,'guestinfo.html',info)





