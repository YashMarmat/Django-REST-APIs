# Django-REST-APIs

A quick guide to create your own Django Apps with Django Rest Apis functionality :)

Steps to follow: 

1) first i created a simple model (basically a blog or post model),

2) registered it in admin file,

3) ran tests,

4) to work on django rest framework i installed it (pipenv install djangorestframework==3.10.3),

5) after installation mention it above your app (heading: third party app),

6) then in bottom of settings.py file mention django rest framework permissions,

7) then project level URL's file for location endpoints (just mentioning paths),

8) then create a url.py file in app level and import classes (created in views.py file) there and then create new paths,

9) dont forget to update urls.py file of project level.

10) then i worked on views.py file (see code) and serializers.py file.

* basically serializers file contain those fields which is to be diplayed on api page.

11) then just run the server and go to http://127.0.0.1:8000/api/v1/ to see the Post List endpoint.
