Notes:

Enable CoreAPI Schema: Django Rest Framework 3.x deprecated the CoreAPI based schema generation and introduced the OpenAPI schema generation in its place. Currently to continue to use django-rest-swagger we need to re-enable the CoreAPI schema. To settings.py add:

REST_FRAMEWORK = 
{'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema' }


Change the swagger index.file: {% load staticfiles %} has been deprecated in django 2.x and removed in 3.x. Modify the same in index.html file of swagger in the location:
Lib\site-packages\rest_framework_swagger\templates\rest_framework_swagger\index.html

Modify {% load staticfiles %} to {% load static %}

pip install PyJWT==1.7.1