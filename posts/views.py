from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
    'content': 'Hello World!'
    }
    return render(request, 'posts/home.html', context)


def postDetails(request):
    context = {
    'content': 'Hello World!'
    }
    return render(request, 'posts/postDetails.html', context)


