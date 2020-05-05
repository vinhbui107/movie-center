from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
    UserChangeForm,
    UsernameField,
)
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import CustomerUser
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
import re


class LoginForm(forms.Form):
    pass


class SignUpForm(UserCreationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password Again'}))

    class Meta:
        model = CustomerUser
        fields = ("username", "email", "address", "phone_number")
        field_classes = {"username": UsernameField}

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Letters and numbers only. Please try again without symbols.")
        if len(username) < 8:
            raise forms.ValidationError("Username has to be longer then 8 characters.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomerUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Your email address is not unique')
        return email


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email", "address", "phone_number", "photo")

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not re.search(r'^\w+$', first_name):
            raise forms.ValidationError("Letters and numbers only. Please try again without symbols.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not re.search(r'^\w+$', last_name):
            raise forms.ValidationError("Letters and numbers only. Please try again without symbols.")
        return last_name


class ChangePasswordForm:
    pass
