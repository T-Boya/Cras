from django.conf.urls import url
from crastinus import views

urlpatterns = [
    url(r'^$', views.index2, name='index2'), 
]
