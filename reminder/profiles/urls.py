from django.conf.urls import url, include
from profiles import views


urlpatterns = [
    url(r'^$', views.index, name='profiles'),
    url(r'^register/$',views.register , name='register'),
    url(r'^login/$', views.authentication, name='authentication'),
]
