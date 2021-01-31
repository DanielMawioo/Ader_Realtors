from django.conf.urls import url
from django.urls import path

from .views import (
        PropertyListView, 
        PropertyDetailSlugView, 
        PropertyCreateView,
        PropertyUpdateView,
        PropertyRatingView,
        UserFavoriteProperty,
        # ContactView,
        # AboutView
)
from .import views



app_name = 'property'

urlpatterns = [
    path('',PropertyListView.as_view(),name='list'),
    # path('create/',views.create_property,name='create'),
    path('(<slug>[\w-]+)/',PropertyDetailSlugView.as_view(),name='details'),
    path('(<slug>[\w-]+)/edit/',PropertyUpdateView.as_view(),name='edit'),
    path('ajax/rating/', PropertyRatingView.as_view(), name='ajax_rating'),
    path('city/(<slug>[\w-]+)/', views.get_city, name ="city"),
    path('city/(<slug>[\w-]+)/(<neighborhood_slug>[\w-]+)/', views.get_neighborhood, name ="neighborhood"),
]
