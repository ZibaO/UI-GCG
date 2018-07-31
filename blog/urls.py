from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^signup/$', views.signup,{'template_name': 'registration/signup.html', 'next_page': 'registration/home.html'}, name='signup'),
    url(r'^login/$', auth_views.login,name='login'),
    url(r'^home/$', views.home, name='home'),
    url(r'^editProfile/$', views.editProfile, {'template_name': 'registration/editProfile.html'}, name='editProfile'),
    url(r'^logout/$', views.logout, {'template_name': 'registration/logout.html'}, name='logout'),
    url(r'^Request/$', views.Request, {'template_name': 'registration/Request.html'}, name='Request'),

]