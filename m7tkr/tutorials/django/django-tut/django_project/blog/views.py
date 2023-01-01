from django.shortcuts import render
<<<<<<< HEAD
from .models import Post
=======

posts = [
    {
        'author': 'mhmmd',
        'content': 'sciences',
        'comment': 'evrthin is illusionary',
        'date_posted': 'August 28, 2022'
    },
    {
        'author': 'bakr',
        'content': 'poems',
        'comment': 'evr is illusionary',
        'date_posted': 'August 20, 2022'
    }
]
>>>>>>> 6d69347 (django tutorials started)


def home(request):

    context = {
<<<<<<< HEAD
        'posts': Post.objects.all()
=======
        'posts': posts
>>>>>>> 6d69347 (django tutorials started)
    }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
