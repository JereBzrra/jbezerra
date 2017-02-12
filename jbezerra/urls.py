from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.jb_index, name='jb_index'),
    url(r'^home/$', views.slide_home, name='slide_home'),
    url(r'^obras/(?s).*', views.obra_list, name='obra_list'),
    #url(r'^obras/(?P<pk>[0-9]+)/$', views.obra_item, name='obra_item'),
    url(r'^biografia/$', views.jb_biografia, name='jb_biografia'),
    url(r'^criticas/$', views.critica_list, name='critica_list'),
    url(r'^contato/$', views.jb_contato, name='jb_contato'),
]
