from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'interviews'

urlpatterns = [
    path('', views.interview_list, name='interview_list'),
    path('detail/<str:name_list>/',  views.interview_detail, name='interview_detail'),
]