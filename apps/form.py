from django import forms
from django.forms import ModelForm

from apps.models import User, Email


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'



class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = ['email']