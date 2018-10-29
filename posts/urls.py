from django.conf.urls import url
from . import views
from posts.models import Posts
from django.urls import path

urlpatterns=[
	path('logout', views.logout, name = "logout"),
 ]