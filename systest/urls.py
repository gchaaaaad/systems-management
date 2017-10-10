from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.system_list, name='system_list'),
    url(r'^system_versions/(?P<pk>\d+)/$', views.system_versions, name='system_versions'),
    
]