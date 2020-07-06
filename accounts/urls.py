from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls import url

urlpatterns = [
    path('',views.indexView,name="home"),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(next_page='dashboard'),name="logout"), 

    ################

   # path('index', views.index, name="index"),
	url('afficheclient/(?P<id>.+)', views.afficheclient, name="afficheclient"),
	path('addclient', views.addclient, name="addclient"),
	url('editeclient/(?P<id>.+)', views.editeclient, name="editeclient"),
	url('deleteclient/(?P<id>.+)', views.deleteclient, name="deleteclient"),
	#Gestion Livraison
	url('leurlivraison/(?P<id>.+)', views.leurlivraison, name="leurlivraison"),
	url('addlivraison/(?P<id>.+)', views.addlivraison, name="addlivraison"),
	url('editelivraison/(?P<id>.+)/(?P<id_liv>.+)', views.editelivraison, name="editelivraison"),
	url('deletelivraison/(?P<id>.+)/(?P<id_liv>.+)', views.deletelivraison, name="deletelivraison"),
]
 