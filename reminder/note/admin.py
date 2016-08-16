from django.contrib import admin
from note.models import Reminder, Group
# Register your models here.


class GroupAdmin(admin.ModelAdmin):
    fields = ('user', 'name')
    filter_horizontal = ('user',)

class ReminderAdmin(admin.ModelAdmin):
    fields = ('user', 'name')
    filter_horizontal = ('user',)

admin.site.register(Reminder, ReminderAdmin)
admin.site.register(Group, GroupAdmin)
