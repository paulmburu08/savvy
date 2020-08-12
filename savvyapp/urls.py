from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url('^$', views.index,name='index'),
    url(r'^neighborhood/([A-Za-z]+)',views.neighborhoods,name ='neighborhood'),
    path('send/email', views.send_email, name='email'),
    path('new/profile', views.new_profile, name='new_profile'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('new/post/<int:id>', views.new_post, name='new_post'),
]