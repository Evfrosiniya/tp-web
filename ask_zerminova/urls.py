from django.conf.urls import patterns, include, url
from django.contrib import admin
from application import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^hot/(?P<page>\d+)/$', views.hot_index, name='hot_index'),
    #url(r'^hot/$', views.hot_index, name='hot_index'),

    url(r'^tag/(?P<tag>\d+)//(?P<page>\d+)/$', views.tag_index, name='tag_index'),
    #url(r'^tag/$', views.tag_index, name='tag_index'),

    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^ask/$', views.ask, name='ask'),

    url(r'^question/(?P<question_id>\d+)/(?P<page>\d+)/$', views.question, name='question'),
    #url(r'^question/(?P<page>\d+)/$', views.question, name='question'),
    #url(r'^question/$', views.question, name='question'),

    url(r'^(?P<page>\d+)/$', views.index, name='index'),
    #url(r'^$', views.index, name='index'),
]