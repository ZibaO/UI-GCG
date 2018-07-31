
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Request


class SignUpForm(forms.ModelForm):
    #birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email','phone_number','national_number','password' )



class RequestForm(forms.ModelForm):

    date_requested  = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = Request
        fields = ('writer', 'text')

