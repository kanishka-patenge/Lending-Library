from django.urls import path
from . import views

urlpatterns = [
    path('',views.choice,name='choice'),
	path('add',views.add,name='add'),
    path('delete',views.delete,name='delete'),
    path('copiesadd',views.copiesadd,name="copiesadd"),
    path('copiesremove',views.copiesremove,name='copiesremove'),
    path('signup',views.signup,name='signup'),
    path('stulogin',views.stulogin,name='stulogin'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('lend',views.lend,name='lend'),
    path('returnbook',views.returnbook,name = 'returnbook'),
    path('stuhome',views.stuhome,name='stuhome'),
    path('stulogout',views.stulogout,name='stulogout'),
    path('adminlogout',views.adminlogout,name='adminlogout')
	
]
