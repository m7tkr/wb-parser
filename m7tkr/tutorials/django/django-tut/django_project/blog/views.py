from django.shortcuts import render
<<<<<<< HEAD
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
=======
from .models import Post
>>>>>>> a05e9fd (django models)


def home(request):

    context = {
<<<<<<< HEAD
<<<<<<< HEAD
        'posts': Post.objects.all()
=======
        'posts': posts
>>>>>>> 6d69347 (django tutorials started)
=======
        'posts': Post.objects.all()
>>>>>>> a05e9fd (django models)
    }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
