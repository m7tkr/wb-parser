from django.shortcuts import render

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


def home(request):

    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
