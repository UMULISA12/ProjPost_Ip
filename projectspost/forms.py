from django import forms
from .models import Project,Profile

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['profile','usability','design','content']

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

        exclude = ['profile']
        
class VoteForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['link','description','profile','image','title']