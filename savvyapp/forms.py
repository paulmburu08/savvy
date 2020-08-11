from django import forms
from .models import UserProfile

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
        fields = ['location' , 'profile_pic', 'bio', 'email']
        widgets = {
            'email' : forms.EmailInput(),
        }