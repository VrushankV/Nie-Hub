from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from posts.models import *
from events.models import *
from books.models import *
from django.contrib import messages
from django.contrib.auth import logout
# Create your views here.

def home(request):
      return render(request,'nie_hub/home.html',{})


def login(request):
      if request.method=='POST':
            m = User.objects.get(usn=request.POST['uname'])
            if m.password == request.POST['pass']:
                  request.session['usn'] = m.usn
                  request.session['category'] = m.category
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
      if request.session.get('usn') != None:
            return render(request,'nie_hub/main.html')
      else:
            return HttpResponse("<h2>You are not logged in<h2>")      


def logout_view(request):
      logout(request)
      return redirect("login")

def myprofile(request):
      uid = User.objects.get(usn = request.session['usn'])
      return render(request,"nie_hub/myprofile.html",{"uid":uid}) 

def mybooks(request):
      if request.method == 'POST':
            for key,value in request.POST.items():
                  if key[:6]=="submit":
                        k=int(key[6:])
            uid = User.objects.get(usn = request.session['usn'])
            bdid = Book_details.objects.get(book_details_id=k)
            bid=Books.objects.get(book_id=bdid.book_id.book_id).delete()
            bdid = Book_details.objects.filter(owner_id=uid)
            length=len(bdid)
            return render(request,'nie_hub/mybooks.html',{"bdid":bdid,"length":length})
      else:
            uid = User.objects.get(usn = request.session['usn'])
            bdid = Book_details.objects.filter(owner_id=uid)
            length=len(bdid)
            return render(request,'nie_hub/mybooks.html',{"bdid":bdid,"length":length})

def myevents(request):
      if request.method == 'POST':
            for key,value in request.POST.items():
                  if key[:6]=="submit":
                        k=int(key[6:])
            uid = User.objects.get(usn = request.session['usn'])
            eid = Events.objects.get(event_id=k).delete()
            eid = Events.objects.filter(owner_id=uid)
            length=len(eid)
            return render(request,'nie_hub/myevents.html',{"eid":eid,"length":length})
      else:
            uid = User.objects.get(usn = request.session['usn'])
            eid = Events.objects.filter(owner_id=uid)
            length=len(eid)
            return render(request,'nie_hub/myevents.html',{"eid":eid,"length":length})    

def myposts(request):
      if request.method == 'POST':
            for key,value in request.POST.items():
                  if key[:6]=="submit":
                        k=int(key[6:])
            uid = User.objects.get(usn = request.session['usn'])
            pid=Posts.objects.get(post_id=k).delete()
            pid=Posts.objects.filter(user_id=uid)
            aid=Attachments.objects.filter(post_id__in=pid)
            length=len(pid)
            return render(request,'nie_hub/myposts.html',{"pid":pid,"aid":aid,"length":length})
      else:
            uid = User.objects.get(usn = request.session['usn'])
            pid=Posts.objects.filter(user_id=uid)
            aid=Attachments.objects.filter(post_id__in=pid)
            length=len(pid)
            return render(request,"nie_hub/myposts.html",{"pid":pid,"aid":aid,"length":length}) 

def change(request):
      uid = User.objects.get(usn = request.session['usn'])
      return render(request,'nie_hub/change.html',{"uid":uid})


def changed(request):
      if request.method=='POST':
             uid = User.objects.get(usn = request.session['usn'])
             if uid.password != request.POST.get('password0'):
                  return render(request,"nie_hub/changed.html",{"msg":"The Current Password you entered is wrong"})
             else:
                  if request.POST.get('password1') == request.POST.get('password2'):
                        return render(request,"nie_hub/changed.html",{"msg":"Password changed successfully!"})
                  else:
                        return render(request,"nie_hub/changed.html",{"msg":"The Passwords you entered don't match!"})