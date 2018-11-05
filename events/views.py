from django.shortcuts import render,redirect
from nie_hub.models import User
from .models import Events,Items,Item_details,Transaction_items
from django.utils import timezone 

# Create your views here.
def create1(request):
      if request.method == 'POST':
            uid = User.objects.get(usn = request.session['usn'])
            events=Events()
            events.name = request.POST.get('ename')
            events.body= request.POST.get('body')
            events.event_date= request.POST.get('edate')
            events.venue= request.POST.get('venue')
            events.create_date=timezone.now()
            events.owner_id=uid
            events.save()
            return render(request,"events/create_event2.html",{'events':events})
      else:
            return render(request,"events/create_event1.html", {})

def create2(request):
      if request.method == "POST":
            type_count = int(request.POST.get('types'))
            iname=[]
            category = []
            for i in range(type_count):
                  item_name = 'iname' + (str(i))
                  category_name = 'category' + (str(i))
                  iname.append(request.POST.get(item_name))
                  category.append(request.POST.get(category_name))
            print(request.POST.items())      
            return redirect("main")
      else:
            return render(request,"events/create_event2.html",{})

def manage(request):
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

def event_view(request):  
	if request.session.get('usn') != None:
		return render(request,'nie_hub/main.html')
	else:
	    return HttpResponse("<h2>You are not logged in<h2>")

def transaction_items(request):  
	if request.session.get('usn') != None:
		return render(request,'nie_hub/main.html')
	else:
	    return HttpResponse("<h2>You are not logged in<h2>")
