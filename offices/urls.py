from django.conf.urls import url
from . import views

app_name = 'offices'
urlpatterns = [
 #   url(r'^(?P<pk>[0-9]+)/$', views.DocContentView.as_view(), name = 'contentdoc'),
    url(r'^add/([\w-]+)$', views.OfficeCreateView.as_view(), name = 'add'),
    url(r'^(?P<pk>[0-9]+)/edit$', views.OfficeUpdateView.as_view(), name = 'edit'),
    url(r'^(?P<pk>[0-9]+)/delete$', views.OfficeDeleteView.as_view(), name = 'delete'),
]
