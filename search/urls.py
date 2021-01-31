from django.conf.urls import url
from django.urls import path

from property import views
from search.views import SearchPropertyListView

app_name = 'search'


urlpatterns =[
     path('',SearchPropertyListView.as_view(),name='search-query'),
#      path('/(?P<pk>\d+)/',ProductDetailView.as_view(),name='product-details'),
     
]