from django.conf.urls import include, url
from django.contrib import admin

from .views import (
        TagDetailView,
        TagListView,
        )


app_name ='tag'


urlpatterns = [
    url('', TagListView.as_view(), name='list'),
    url('(<slug>[\w-]+)/', TagDetailView.as_view(), name='detail'),
] 