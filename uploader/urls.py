from django.conf.urls import url
from django.urls import reverse
from . import views

urlpatterns = [
				url(r'^home/$',views.home,name='home'),
				url(r'^login/$',views.Login,name='login'),
				url(r'^$',views.Signup,name='signup'),
				url(r'^logout/$',views.Logout,name='logout'),
				url(r'^upload/$',views.upload,name='upload'),
				 
			]

