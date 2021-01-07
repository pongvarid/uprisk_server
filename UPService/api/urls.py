from django.conf.urls import include, url
from UPService.api import views
from django.urls import path


urlpatterns = [

  url(r'^agencytype/(?P<id>[0-9]+)/$', views.AgencyTypeAPIView.as_view()),
  url(r'^agencytype/$', views.AgencyTypeAPIListView.as_view()),

  url(r'^agency/(?P<id>[0-9]+)/$', views.AgencyAPIView.as_view()),
  url(r'^agency/$', views.AgencyAPIListView.as_view()),

  url(r'^profile/(?P<id>[0-9]+)/$', views.ProfileAPIView.as_view()),
  url(r'^profile/$', views.ProfileAPIListView.as_view()),

  url(r'^year/(?P<id>[0-9]+)/$', views.YearAPIView.as_view()),
  url(r'^year/$', views.YearAPIListView.as_view()),

  url(r'^mission/(?P<id>[0-9]+)/$', views.MissionAPIView.as_view()),
  url(r'^mission/$', views.MissionAPIListView.as_view()),

  path('choices/<str:name>/', views.ChoiceCustomAPIView.as_view()),
  url(r'^choice/(?P<id>[0-9]+)/$', views.ChoiceAPIView.as_view()),
  url(r'^choice/$', views.ChoiceAPIListView.as_view()),

  url(r'^rmplan/(?P<id>[0-9]+)/$', views.RmPlanAPIView.as_view()),
  url(r'^rmplan/$', views.RmPlanAPIListView.as_view()),

  url(r'^riskrm/(?P<id>[0-9]+)/$', views.RiskRMAPIView.as_view()),
  url(r'^riskrm/$', views.RiskRMAPIListView.as_view()),

]
