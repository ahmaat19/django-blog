from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='home'),
    path('post-details/<slug:slug>', views.postDetails, name='post-details'),
]