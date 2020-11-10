from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='home'),
    path('post-details/<slug:slug>', views.postDetails, name='post-details'),
    path('post/add/', views.PostCreateView, name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView, name='post-update'),



    path('category/', views.CategoryViewList, name='category'),
    path('category/add/', views.CategoryCreateView, name='category-create'),
    path('category/<int:pk>/update/', views.CategoryUpdateView, name='category-update'),
    # path('category/<int:pk>/detail/', views.CategoryCreateView, name='category-detail'),
]