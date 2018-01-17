from django.conf.urls import url,re_path
from . import views

urlpatterns = [
    url('^$', views.index, name = 'index'),
    re_path('^details/(?P<ticketId>[0-9])/$', views.details, name = 'details')
];