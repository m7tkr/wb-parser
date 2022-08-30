from django.urls import path
from . import views
<<<<<<< HEAD
<<<<<<< HEAD
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

=======
>>>>>>> 6d69347 (django tutorials started)
=======
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

>>>>>>> a05e9fd (django models)

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
