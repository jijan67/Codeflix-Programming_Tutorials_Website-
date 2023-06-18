from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *
from .models import Course
import stripe
from datetime import datetime, timedelta
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'Registration.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def paymentpage(request):

    return render (request,'payment.html')
def course(request):
    return render (request,'course.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        contact=Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
    return render(request, "contact.html")



def video(request):
    index=Video.objects.all()

    return render(request,"video.html")

def python(request):
    return render (request,'python.html')

def about(request):
    return render (request,'about.html')

def basic(request):
    return render (request,'basic.html')

def search(request):
    query=request.GET['query']
    course = Course.objects.filter(title__icontains=query)
    context = {'course': course}
    return render(request, 'search.html', context)


def base(request):
   return render(request,'base.html')

def Tutorial(request):
    course = Course.objects.all()
    context = {'course': course}
    print(context)
    return render(request, 'Tutorial.html' , context)

def subs(request):
    if request.method == 'POST':
        membership = request.POST.get('membership' , 'MONTHLY')
        amount = 1000
        if membership == 'YEARLY':
            amount = 11000
        stripe.api_key = 'sk_test_qu7ivgHp9WRHlHJjs2QHugIA00hKFbC5qc'

        customer = stripe.Customer.create(
            email = "jisanurrahman48@gmail.com",
			name=request.user.username,
            source=request.POST['stripeToken']
			)
            
        charge = stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency='inr',
			description="Membership",   
		)
        
        print(charge['amount'])
        if charge['paid'] == True:
            profile = Profile.objects.filter(user = request.user).first()
            if charge['amount'] == 100000:
                profile.subscription_type = 'M'
                profile.is_pro = True
                expiry = datetime.now() + timedelta(30)
                profile.pro_expiry_date = expiry
                profile.save()
                
            elif charge['amount'] == 1100000:
                profile.subscription_type = 'Y'
                profile.is_pro = True
                expiry = datetime.now() + timedelta(365)
                profile.pro_expiry_date = expiry
                profile.save()
        
        print(charge)
        return redirect('charge')
   
    return render(request, 'subs.html')

def charge(request):
   return render(request,'charge.html')

def case(request):
   return render(request,'case.html')

def pypage1(request):
   return render(request,'pypage1.html')





