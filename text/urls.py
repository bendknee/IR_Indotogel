from django.urls import re_path, path
from .views import index,query
#url for app
urlpatterns = [
    re_path(r'^$', index, name='index'),
    path(r'query/', query, name='query')
]
