from .models import Image,Profile,Comment
from django import forms

class NewImageForm(forms.ModelForm):
    class Meta:
        model=Image
        exclude=['profile','pub_date','name','likes','comments']

class NewProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['commenter']