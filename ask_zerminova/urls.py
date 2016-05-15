from django.conf.urls import patterns, include, url
from django.contrib import admin
from application import views as ask_zerminova

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^hot/(?P<page>\d+)/$', 'ask_zerminova.views.hot_index', name='hot_index'),
    url(r'^hot/$', 'ask_zerminova.views.hot_index', name='hot_index'),

    url(r'^tag/(?P<tag>\d+)//(?P<page>\d+)/$', 'ask_zerminova.views.tag_index', name='tag_index'),
    url(r'^tag/$', 'ask_zerminova.views.tag_index', name='tag_index'),

    url(r'^signup/$', 'ask_zerminova.views.signup', name='signup'),
    url(r'^login/$', 'ask_zerminova.views.login', name='login'),
    url(r'^ask/$', 'ask_zerminova.views.ask', name='ask'),

    url(r'^question/(?P<question_id>\d+)/(?P<page>\d+)/$', 'ask_zerminova.views.question', name='question'),
    url(r'^question/(?P<page>\d+)/$', 'ask_zerminova.views.question', name='question'),
    url(r'^question/$', 'ask_zerminova.views.question', name='question'),

    url(r'^(?P<page>\d+)/$', 'ask_zerminova.views.index', name='index'),
    url(r'^$', 'ask_zerminova.views.index', name='index'),
]