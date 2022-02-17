from re import A
from django.urls import path, include, reverse
from . import views
from django.contrib.auth import views as auth_views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('medved/privet', views.medved, name='medved'),
    #path('artist/<int:artist_id>/', views.view_artist, name='view_artist'),
    #path('judge/<int:judge_id>/', views.view_judge, name='view_judge'),
    path('dude/<int:dude_id>/', views.view_dude, name='view_dude'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page = '/accounts/login/'), name='logout'),
    path('accounts/register/', views.RegisterFormView.as_view(), name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='polls/login.html', next_page='/myprofile'), name = 'login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('myprofile', views.view_my_profile, name = 'myprofile'),
    path('myprofile/addsong', views.add_song, name = 'add_song'),
    path('myprofile/addreview', views.add_review, name = 'add_review'),
    
]

