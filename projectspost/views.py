from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image,Profile,Comment
from django.core.exceptions import ObjectDoesNotExist
from .forms import NewImageForm,NewProfileForm,NewCommentForm

# Create your views here.

@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user=request.user

    photos=Image.get_photos()
    comments=Comment.get_comments()
    profiles = Profile.objects.all()


    return render(request,'welcome.html',{"photos":photos,"profiles":profiles,"comments":comments})

def imagedetails(request,image_id):
    comments=Comment.objects.filter(image_id=image_id)


    try:
        image = Image.objects.get(id=image_id)
    except ObjectDoesNotExist:
         raise Http404()
    return render(request,"post_details.html",{"image":image,"comments":comments})

def profiledetails(request,profile_id):
    try:
        profile = Profile.objects.get(id=profile_id)
    except ObjectDoesNotExist:
        message = "You haven't searched for any term"


    return render(request,"profiledetails.html",{"profile":profile})



def new_image(request):
    current_user=request.user
    if request.method == 'POST':
        form =NewImageForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.profile = current_user
            image.save()
        return redirect('welcome')
    else:
        form=NewImageForm()
    return render(request,'new_post.html',{"form":form})


def new_comment(request):
    current_user=request.user
    if request.method == 'POST':
        form =NewCommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment=form.save(commit=False)

            comment.commenter = current_user

            comment.save()

        return redirect('welcome')
    else:
        form=NewCommentForm()
    return render(request,'add_comment.html',{"form":form})





def profile(request):
    current_user=request.user
    photos=Image.objects.filter(profile=current_user)
    try:
        profile = Profile.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('create-profile')

    return render(request,'profile.html',{"photos":photos,"profile":profile})





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


def search_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term=request.GET.get("profile")
        searched_profiles=Profile.search_by_user(search_term)
        # message=f"{search_term}"

        return render(request, 'search.html',{"profiles": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})



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