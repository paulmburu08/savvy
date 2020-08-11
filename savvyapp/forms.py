from django import forms
from .models import UserProfile,Posts

LOCATION = [
    ('cbd','CBD'),
    ('westlands','Westlands'),
    ('makadara','Makadara'),
    ('kasarani','Kasarani'),
    ('pumwani','Pumwani'),
    ('kibera','Kibera'),
    ('karen','Karen'),
    ('dagoretti','Dagoretti'),
]

class ProfileForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATION, widget=forms.RadioSelect())
    class Meta:
        model = UserProfile
        exclude = ['user','creat_at','updated_at']
        fields = ['profile_pic', 'bio', 'email','location']
        widgets = {
            'email' : forms.EmailInput(),
        }

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ['user','creat_at','updated_at']
        widgets = {
            'title' : forms.CharField()
        }