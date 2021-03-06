from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Project,Profile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import NewProjectForm,NewProfileForm, VoteForm

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Project

from .serializer import ProjectSerializer,ProfileSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly


@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user = request.user
    projects = Project.get_all()
    return render(request,'welcome.html',{'projects':projects})


def project(request,project_id):
    project = Project.objects.get(id = project_id)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid:
           
            project.save()
    else:
        form = VoteForm()
    return render(request,'project.html',{'form':form,'project':project})



@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = current_user
            project.save()
        return redirect('welcome')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})



def profile(request):
    current_user=request.user
    projects=Project.objects.filter(profile=current_user)
    try:
        profile = Profile.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('profile_create')

    return render(request,'profile.html',{"projects":projects,"profile":profile})



def edit_profile(request):
    current_user=request.user
    if request.method == 'POST':
        form =NewProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user = current_user
            profile.update()
        return redirect('profile')
    else:
        form=NewProfileForm()
    return render(request,'edit_profile.html',{"form":form})


def create_prfle(request):
    current_user=request.user
    if request.method == 'POST':
        form =NewProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')
    else:
        form=NewProfileForm()
    return render(request,'profile-create.html',{"form":form})



def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        # message = f"{search_term}"

        return render(request, 'all-proposts/search.html',{"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-proposts/search.html',{"message":message})


def view_project(request,project_id):
    try :
        project = Project.objects.get(id = project_id)

    except ObjectDoesNotExist:
        raise Http404()
       

    return render(request, 'project-detail.html', {'project':project})


class ProjectList(APIView):

    def get(self, request, format=None):
        all_merch = Project.objects.all()
        serializers = ProjectSerializer(all_merch, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
       
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        permission_classes = (IsAdminOrReadOnly,)





class ProfileList(APIView):
    def get(self, request, format=None):
        all_merch = Profile.objects.all()
        serializers = ProfileSerializer(all_merch, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
       
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        permission_classes = (IsAdminOrReadOnly,)

