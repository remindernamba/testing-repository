from django import forms
from note.models import Group, Reminder

class CreateGroup(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('name', 'user',)


class CreateIncome(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ('date_of_start', )
