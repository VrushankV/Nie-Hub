from django.urls import path
from . import views

urlpatterns = [
	path('create1',views.create1, name="create1"),
	path('create2',views.create2, name="create2"),
	path('manage', views.manage, name="manage"),
	path('event_view',views.event_view, name="event_view"),
	path('transaction_items',views.transaction_items,name="transaction_items"),
]