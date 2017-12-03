from django.conf.urls import url
from . import views

app_name = 'docs'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.DocContentView.as_view(), name = 'contentdoc'),
    url(r'^add/([\w-]+)$', views.DocCreateView.as_view(), name = 'add'),
    url(r'^(?P<pk>[0-9]+)/edit$', views.DocUpdateView.as_view(), name = 'edit'),
    url(r'^(?P<pk>[0-9]+)/delete$', views.DocDeleteView.as_view(), name = 'delete'),
]
