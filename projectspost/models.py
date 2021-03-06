from django.db import models
from django.core.validators import URLValidator
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'projects/', null = True)
    description = models.TextField(max_length = 500)
    link = models.TextField(validators=[URLValidator()],null=True)
    profile = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    
    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def get_all(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def get_project(cls, project_id):
        project = cls.objects.get(id=project_id)
        return project

    @classmethod
    def search_by_title(cls,search_term):
        projects_title = cls.objects.filter(title__icontains=search_term)
        return projects_title

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile/', null = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    bio = models.TextField(max_length = 100, null = True)
    contact = models.IntegerField(null = True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

