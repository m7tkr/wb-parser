# Django Notes

## Loading Page

1. First checks urlpatterns in projects urls.py
2. Chops off matching part, sends remaining part to apps urls.py
3. Checks urlpatterns in app urls.py
4. Chops off matching part, and so on
5. Views.py for displaying HttpResponse using func()

> reason behind this is you can change route in one place, changes apply to daugther routes

## templates subdir

django_project -> appNameDir -> templatesDir -> appNameDir -> template.html

1. add blog app to list of installed apps, thus django know to search for it in templates dir
2. add apps.py config to projects settings.py

always check for repeate code

1. template inheritance
2. static folder for static css and js in app dir with

django_project -> appNameDir -> static -> appNameDir -> style.css
