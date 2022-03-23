from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm,Textarea, IntegerField
from .models import *

#Create the forms

class NewUserForm(UserCreationForm):
    # email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username","email","password1","password2")
        
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ("name","occupation","profile_image","Location","email")


class LocalForm(forms.ModelForm):
    class Meta:
        model = Locals
        fields =("name","Location","email")