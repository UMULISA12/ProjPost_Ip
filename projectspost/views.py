from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Project,Profile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import NewProjectForm,NewProfileForm, VoteForm
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serializer import ProjectSerializer, ProfileSerializer
# Create your views here.

@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user = request.user
    projects = Project.get_all()
    return render(request,'welcome.html',{'projects':projects})


def project(request,project_id):
    project = Project.objects.get(id = project_id)
    rating = round(((project.design + project.usability + project.content)/3),2)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid:
            # if project.design == 1:
            #     project.design = int(request.POST['design'])
            # else:
            #     project.design = (project.design + int(request.POST['design']))/2
            # if project.usability == 1:
            #     project.usability = int(request.POST['usability'])
            # else:
            #     project.usability = (project.design + int(request.POST['usability']))/2
            # if project.content == 1:
            #     project.content = int(request.POST['content'])
            # else:
            #     project.content = (project.design + int(request.POST['content']))/2
            project.save()
    else:
        form = VoteForm()
    return render(request,'project.html',{'form':form,'project':project,'rating':rating})




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



# def vote_project(request, project_id):
#     project = Project.objects.get(id=project_id)
#     rating = round(((project.design + project.usability + project.content)/3),2)
#     if request.method == 'POST':
#         form = VoteForm(request.POST)
#         if form.is_valid:
#             if project.design == 1:
#                 project.design = int(request.POST['design'])
#             else:
#                 project.design = (project.design + int(request.POST['design']))/2
#             if project.usability == 1:
#                 project.usability = int(request.POST['usability'])
#             else:
#                 project.usability = (project.design + int(request.POST['usability']))/2
#             if project.content == 1:
#                 project.content = int(request.POST['content'])
#             else:
#                 project.content = (project.design + int(request.POST['content']))/2
#             project.save()
#     else:
#         form = VoteForm()
#     return render(request,'vote.html',{'form':form,'project':project,'rating':rating})




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



def profiledetails(request,profile_id):
    try:
        profile = Profile.objects.get(id=profile_id)
    except ObjectDoesNotExist:
        message = "You haven't searched for any term"


    return render(request,"profiledetails.html",{"profile":profile})



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
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-proposts/search.html',{"message":message})



def view_project(request,project_id):
    try :
        project = Project.objects.get(id = project_id)

    except ObjectDoesNotExist:
        raise Http404()
        # return render(request, 'no_project.html')

    return render(request, 'project-detail.html', {'project':project})


# class ProjectList(APIView):
#     def get(self, request, format=None):
#         all_project =Project.objects.all()
#         serializers = ProjectSerializer(all_project, many=True)
#         return Response(serializers.data)

# class ProfileList(APIView):
#     def get(self, request, format=None):
#         all_profile =Profile.objects.all()
#         serializers = ProfileSerializer(all_profile, many=True)
#         return Response(serializers.data)