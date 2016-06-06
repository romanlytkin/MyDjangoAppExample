
from django.conf.urls import include, url
from django.contrib import admin
from app.comment import comment
from app.statistic import stat
from app.views import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', comment.index, name='Home'),
    url(r'^comment/$', comment.index, name='Home'),
    url(r'^addcomment/$', comment.addcomment, name='AddComment'),
    url(r'^selectregion/$', comment.selectregion, name='SelectRegion'),
    url(r'^selectorcity/$', comment.selectorcity, name='SelectorCity'),

    url(r'^view/$', views.index, name='View'),
    url(r'^delcomment', views.delcomment, name='DelComment'),

    url(r'^stat/$', stat.index, name='Statictic'),
    url(r'^stat/(?P<region_id>\d+)/$', stat.statbyregion, name='StatByRegion'),
    url(r'^stat/(?P<region_id>\d+)/(?P<city_id>\d+)$', stat.statbycity, name='StatByCity'),
]
