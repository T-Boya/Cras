from django.conf.urls import url
from crastinus import views

urlpatterns = [
    url(r'^$', views.index2, name='index2'),
    url(r'^girly/', views.girl, name='girl'),
    url(r'^help/', views.help, name='help'),
    url(r'^girl2/', views.girl2, name='girl2'),
    url(r'^train/', views.train, name='train'),

]
