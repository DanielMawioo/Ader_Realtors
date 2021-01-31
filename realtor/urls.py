from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from property.views import PropertyCreateView
from property.views import RealtorPropertyListView
from property.views import PropertyUpdateView #PropertyOtherImages
from .import views


from .views import (
        RealtorView,
        RealtorDetailRedirectView,
        # Realtor_Profile,
        RealtorUpdate,
        RealtorsListView,
        RealtorsDetailView,
        RealtorCreate

        
        )

app_name ='realtor'

urlpatterns = [ 
    path('', RealtorView.as_view(), name='home'),
    path('create/', RealtorCreate.as_view(), name='create_reator'),
    path('update/(<pk>\d+)/', RealtorUpdate.as_view(), name='update'),
    path('property/',RealtorPropertyListView.as_view(),name='property_list'),
    path('property/create/',PropertyCreateView.as_view(),name='create'),
    # path('property/add-more-images/',PropertyOtherImages.as_view(),name='add_more_images'),
    path('property/(<pk>\d+)/edit/',PropertyUpdateView.as_view(),name='property_edit'),
    path('property/(<pk>\d+)/',RealtorDetailRedirectView.as_view()),
    path('realtors/', RealtorsListView.as_view(), name='realtors'),
    path('realtors/(<pk>\d+)/', RealtorsDetailView.as_view(), name='realtor-detail'),
   # path('realtor_profile/(<pk>\d+)/', Realtor_Profile.as_view(), name='realtor_profile')
    # path('realtor_profile/', views.realtor_profile, name='realtor_profile')
] 