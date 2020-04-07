# Django-REST-APIs

Basic understanding of Django Rest Apis :)

Here in this project: 

* first i created a simple model (basically a blog or post model),

* registered it in admin file,

* ran tests,

* to work on django rest framework i installed it (pipenv install djangorestframework==3.10.3),

* after installation mention it above your app (heading: third party app),

* then in bottom of settings.py file mention django rest framework permissions,

* then project level URL's file for location endpoints (just mentioning paths),

* then create a url.py file in app level and import classes (created in views.py file) there and then create new paths,

* dont forget to update urls.py file of project level.

* then i worked on views.py file (see code) and serializers.py file.

* basically serializers file contain those fields which is to be diplayed on api page.

* then just run the server and go to http://127.0.0.1:8000/api/v1/ to see the Post List endpoint.
