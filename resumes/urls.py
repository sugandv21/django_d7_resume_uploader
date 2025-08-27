from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_resume, name='submit_resume'),
    path('list/', views.resume_list, name='resume_list'),
]
