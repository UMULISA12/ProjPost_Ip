from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns=[
    url(r'^$',views.welcome,name='welcome'),
    url(r'^projects/(\d+)',views.project,name ='projects'),
    url(r'^new/project$', views.new_project, name='new-project'),
    
    url(r'^create/profile$',views.create_prfle,name='profile_create'),
    url(r'^profile/',views.profile,name='profile'),
    url(r'^profiledetails/(\d+)',views.profiledetails,name ='profiledetails'),

    url(r'^edit/profile$',views.edit_profile,name='edit-profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^project-detail/(\d+)',views.search_project,name = 'project-detail'),
    # url(r'^project-vote/(\d+)',views.vote_project,name = 'project-vote'),
    # url(r'^api/project/$', views.ProjectList.as_view()),
    # url(r'^api/profile/$', views.ProfileList.as_view()),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)