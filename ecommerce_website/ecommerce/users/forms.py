from django import forms
from store.models import Customer
from django.contrib.auth.models import User


class CustomerRegisterForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']