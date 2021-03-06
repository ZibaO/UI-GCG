"""second URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path



from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', views.signup, {'template_name': 'registration/signup.html','next_page':'registration/home.html'}, name='signup'),
    url(r'^login/$', auth_views.login , name='login'),
    url(r'^home/$', views.home,{'template_name': 'registration/home.html'}, name='home'),
    url(r'^editProfile/$', views.editProfile, {'template_name': 'registration/editProfile.html'}, name='editProfile'),
    url(r'^logout/$', views.logout, {'template_name': 'registration/logout.html'}, name='logout'),
    url(r'^Request/$', views.Request, {'template_name': 'registration/Request.html'}, name='Request'),



   # url(r'^signup/$', views.signup,{'template_name': 'registration/signup.html'}, name='signup'),
]
    #url(r'', include('blog.urls')),













