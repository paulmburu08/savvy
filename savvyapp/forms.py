from django import forms
from .models import UserProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user','creat_at']
        widgets = {
            'email' : forms.EmailInput(),
        }