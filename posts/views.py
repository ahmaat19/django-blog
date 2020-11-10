from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Post
from .forms import CategoryModelForm, PostModelForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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



@login_required
def CategoryCreateView(request):   
    form = CategoryModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user.id
        obj.save()
        messages.success(request, 'Category created successfully.')
        return redirect('/category/')

    context = {
        'form': form,
        'valueBtn': 'Add',
        'title': 'Create Category',
    }
    return render(request, 'posts/category-form.html', context) 


@login_required
def CategoryUpdateView(request, pk):   
    cat_id = get_object_or_404(Category, pk=pk)
    form = CategoryModelForm(request.POST or None, instance=cat_id)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user.id
        obj.save()
        messages.success(request, 'Category updated successfully.')
        return redirect('/category/')

    context = {
        'form': form,
        'valueBtn': 'Update',
        'title': 'Update Category',
    }
    return render(request, 'posts/category-form.html', context) 



def CategoryViewList(request):
    cat = Category.objects.order_by('-id')
    paginator = Paginator(cat, 4)  # Show 10 contacts per page
    page = request.GET.get('page')
    categories = paginator.get_page(page)

    context = {
        'categories':categories
    }
    return render(request, 'posts/category.html', context)




@login_required
def PostCreateView(request):   
    form = PostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user.id
        obj.save()
        messages.success(request, 'Post created successfully.')
        return redirect('/')

    context = {
        'form': form,
        'valueBtn': 'Add',
        'title': 'Create Post',
    }
    return render(request, 'posts/post-form.html', context) 


@login_required
def PostUpdateView(request, pk):   
    cat_id = get_object_or_404(Post, pk=pk)
    form = PostModelForm(request.POST or None, request.FILES or None, instance=cat_id)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user.id
        obj.save()
        messages.success(request, 'Post updated successfully.')
        return redirect('/')

    context = {
        'form': form,
        'valueBtn': 'Update',
        'title': 'Update Post',
    }
    return render(request, 'posts/post-form.html', context) 