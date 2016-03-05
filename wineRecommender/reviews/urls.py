from django.conf.urls import url
from django.contrib import admin

#Now we can go through each view itself


# urlpatterns = [
#     url(r'^$', post_list, name='list'),
#     url(r'^create/$', post_create),
#     # New parm with name of id, only accepting digits.
#     url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
#     url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
#     url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),

#     # url(r'^posts/$', "<appname>.views.<function_hame>"),
# ]
from . import views

#  Reviews/
urlpatterns = [
    # ex: /
    url(r'^$', views.review_list, name='review_list'),
    # ex: /review/5/
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /wine/
    url(r'^wine$', views.wine_list, name='wine_list'),
    # ex: /wine/5/
    url(r'^wine/(?P<wine_id>[0-9]+)/$', views.wine_detail, name='wine_detail'),
]