from django.conf.urls import url, include
from organizations import views
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'organizations'
urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^(?P<pk>[\w-]+)/logout/$', views.logout_admin, name='logout'),    
    url(r'^([\w-]+)/$', views.IndexView.as_view(), name = 'index'),
    url(r'^([\w-]+)/feedback/$', views.FeedbackView.as_view(), name = 'feedback'),
    url(r'^([\w-]+)/docs/$', views.DocListView.as_view(), name = 'doc'),
    url(r'^([\w-]+)/offices/$', views.OfficeListView.as_view(), name = 'office'),
    url(r'^(?P<pk>[\w-]+)/admin/$', views.OrgUpdateView.as_view(), name = 'admin'),
  
     
]
