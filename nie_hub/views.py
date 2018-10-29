from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages
# Create your views here.

def home(request):
	return render(request,'nie_hub/home.html',{})


def login(request):
      if request.method=='POST':
            m = User.objects.get(usn=request.POST['uname'])
            if m.password == request.POST['pass']:
                  request.session['usn'] = m.usn
                  messages.success(request, "Welcome")
                  return redirect("main")
            else:
                  messages.error(request, "Password does not match")
                  return redirect("login")
      else: 
            return render(request,"nie_hub/login.html", {})



def signup(request):
      if request.method == 'POST':
            user=User()
            user.first_name = request.POST.get('fname')
            user.last_name= request.POST.get('lname')
            user.branch= request.POST.get('branch')
            user.sem= request.POST.get('sem')
            user.address= request.POST.get('address')
            user.email= request.POST.get('email')
            user.phone_number= request.POST.get('phone_number')
            user.usn= request.POST.get('usn')
            user.password= request.POST.get('password')
            user.category= request.POST.get('category')
            user.save()
            return redirect("login")
      else: 
            return render(request,'nie_hub/signup.html',{})



def main(request):
      return render(request,'nie_hub/main.html')


