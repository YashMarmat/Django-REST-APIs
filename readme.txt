-Here in this project:

first i created a simple model,
registered it in admin file,
ran tests,
to work on django rest framework i installed it (pipenv install djangorestframework==3.10.3),
after installation mention it above your app (heading: third party app),
then in bottom of settings.py file mention django rest framework permissions,
then project level URL's file for location endpoints (just mentioning paths),
then create a url.py file in app level and import classes of views their and also work on paths,
before that work on views.py file and serializers.py file.
then just run the server and go to http://127.0.0.1:8000/api/v1/ to see the Post List endpoint.


# Total Apps (all projects) to be install in the end of this Django Rest Api Series are:

pipenv install djangorestframework==3.10.3

pipenv install django-rest-auth==0.9.5     (for sepeate login and logout features on api page)

pipenv install django-allauth==0.40.0      (for signup or registration page)
