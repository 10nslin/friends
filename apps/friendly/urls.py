from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
    url(r'^dashboard$', views.dashboard),
    url(r'^user/(?P<user_id>\d+)/$', views.show),
    url(r'^add/(?P<friend_id>\d+)/$', views.add),
    url(r'^remove/(?P<friend_id>\d+)/$', views.remove),
 
]