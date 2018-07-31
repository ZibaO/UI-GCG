from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm
from .forms import RequestForm



@login_required
def home(request,template_name):
    return render(request, 'registration/home.html')

def editProfile(request,template_name):
    return render(request, 'registration/editProfile.html')

def logout(request,template_name):
    return render(request, 'registration/logout.html')

def Request(request,template_name):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            req = form.save()
            req.save()
    else:
        form = RequestForm()
    return render(request, 'registration/Request.html', {'form': form})


   # form = RequestForm()
    #return render(request, 'registration/Request.html', {'form': form})




def signup(request,template_name, next_page):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            #login(request,'registration/login.html','registration/home.html')
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            user.refresh_from_db()  # load the profile instance created by the signal
            # user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            #login(request, 'registration/login.html', 'registration/home.html')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})