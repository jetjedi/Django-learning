#Groups url.py file

from django.conf.urls import url
from . import views

app_name = 'groups'

urlpatterns = [
    url(r'^$', views.ListGroups.as_View(), name='all'),
    url(r'^new/$', views.CreateGroup.as_View(), name='create'),
    url(r'posts/in/(?P<slug>[-\w]+)/$', views.SingleGroup.as_View(), name='single'),
    
]
