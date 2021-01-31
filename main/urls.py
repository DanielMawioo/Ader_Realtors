from django.conf.urls import url
from django.urls import path, include
from django.urls import reverse_lazy
from .import views
from django.contrib.auth import views as auth_views
from main.views import *
from .views import *
from django.contrib.auth.views import LoginView
from property.views import UserFavoriteProperty
from .views import ContactView, AboutView



app_name = 'main'




urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('login/',login,{'template_name':'main/login.html'},name='login'),
    path('login/', LoginView.as_view(template_name='main/login.html'), name='login'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('about/',AboutView.as_view(),name='about'),

    path('login/',LoginView.as_view(),name='login'),

    path('login/',views.login_page,name='login'),

    #path('logout/',logout,{'main/index.html'},name='logout'),
    path('logout/', LoginView.as_view(template_name='main/logout.html'), name='logout'),

    #path('logout/',LogoutView.as_view(),name='logout'),

    path('register/', views.register, name='register'),

    path('change-password/',views.change_password, name="change_password"),
   
    path('profile/',views.user_profile, name="profile"),
    
    #path('reset-password/', password_reset, {'template_name':'main/reset_password.html','email_template_name':'main/reset_password_email.html', 'post_reset_redirect':'main:password_reset_done','from_email':'main@django.com',},name='password_reset'),

   
    #path('reset-password/done/', password_reset_done, {'template_name': 'main/reset_password_done.html'}, name='password_reset_done'),

    #path('reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/',password_reset_confirm, {'template_name':'main/reset_password_confirm.html','post_reset_redirect': reverse_lazy('main:password_reset_complete')},name='password_reset_confirm'),

    #path('reset-password/complete/', password_reset_complete,{'template_name':'main/reset_password_complete.html'}, name='password_reset_complete'),

    path('favorite/',UserFavoriteProperty.as_view(),name='favorite'),

]


