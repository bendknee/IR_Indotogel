from django.urls import path
from .views import index
# url for app
urlpatterns = [
    path(r'', index, name='index'),
]
