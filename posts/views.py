from django.shortcuts import render,redirect
from .models import Posts
from nie_hub.models import User
from .forms import PostForm
from django.utils import timezone
from django.http import HttpResponse

# Create your views here.

def create_post(request):
	if request.method == "POST":
		uid = User.objects.get(usn = request.session['usn'])
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			posts = form.save(commit = False)
			posts.date = timezone.now()
			posts.user_id = uid
			posts.save()
			return redirect("main")	
	else:
		form = PostForm()
		return render(request,'posts/create_post.html',{'form':form})

def view_post(request):
	user = User.objects.get(usn = request.session['usn'])
	all_posts = Posts.objects.filter(sem = user.sem, branch = user.branch).order_by("-date")
	length = len(all_posts)
	return render(request,'posts/view_post.html',{'all_posts':all_posts, 'length':length})

 