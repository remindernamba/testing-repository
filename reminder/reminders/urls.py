from django.conf.urls import url
from reminders import views
urlpatterns = [
    url(r'^$', views.add_group, name='group'),
    url(r'^(?P<group_id>[0-9]+)/reminders_add/$', views.add_reminders, name='reminder'),
    url(r'(?P<group_idi>[0-9]+)/group$', views.reminders_page, name='reminderss'),
    url(r'(?P<del_id>[0-9]+)/delete_remind$', views.del_remind, name='delremind'),
]
