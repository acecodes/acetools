from django.conf.urls import patterns, include, url
from django.contrib import admin
from skillstreak.views import index

urlpatterns = patterns('',
    url(r'^', index),
)
