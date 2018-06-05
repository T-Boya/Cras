from django.conf.urls import url
from crastinus import views

urlpatterns = [
    url(r'^$', views.index, name='index'), 
]