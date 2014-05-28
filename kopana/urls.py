from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from main import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^team/(?P<team_id>\d+)/', views.team, name='team'),
    # url(r'^kopana/', ),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signUp/', views.signUp, name='signUp'),
    url(r'^signIn/', views.signIn, name='signIn'),
    url(r'^seasons/', views.ListSeasons, name='seasons'),

   url(r'^updateSeason/(?P<id>\d+)/', views.SeazonUpdate, name='updateseason'),
   url(r'^updateSeason/', views.SeazonUpdate, name='addseason'),
      url(r'^delSeason/(?P<id>\d+)/', views.delSeason, name='delseason'),
          url(r'^rounds/(?P<id>\d+)', views.ListReasons, name='rounds'),
   url(r'^updateRound/(?P<id>\d+)/', views.RoundUpdate, name='updateround'),
   url(r'^updateRound/', views.RoundUpdate, name='addround'),
      url(r'^delRound/(?P<id>\d+)/', views.delRound, name='delround'),
)
