from django.conf.urls import url
from crastinus import views

urlpatterns = [
    url(r'^$', views.home, name='index'),
    # url(r'^login/$', views.login, name='login') 
]