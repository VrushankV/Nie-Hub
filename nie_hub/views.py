from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'nie_hub/home.html',{})

def login(request):
	return render(request,'nie_hub/login.html',{})	

def signup(request):
	return render(request,'nie_hub/signup.html',{})
