from django.shortcuts import render, get_object_or_404
from .models import Category, Post
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.
def index(request):
     
    post_lists = Post.objects.order_by('-id')
    categories = Category.objects.order_by('-id')
        
    featured_posts = Post.objects.order_by('-id')[:3]

    paginator = Paginator(post_lists, 4)  # Show 10 contacts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'posts': posts,
        'featured_posts': featured_posts,
        'categories':categories
    }
    return render(request, 'posts/home.html', context)


def postDetails(request, slug):
    post = get_object_or_404(Post, slug=slug)
    print(post.title)
    context = {
    'post': post
    }
    return render(request, 'posts/postDetails.html', context)


