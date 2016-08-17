from django.conf.urls import url
from register import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.authentication, name='login')
]
