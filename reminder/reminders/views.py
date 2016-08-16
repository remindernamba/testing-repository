#coding: utf-8
from django.shortcuts import render
from note.models import Reminder, Group
from profiles.models import Profile
from reminders.forms import CreateGroup
from django.shortcuts import redirect
from django.contrib import messages
from profiles import views
from reminders.forms import CreateIncome


def add_group(request):
    profile = Profile.objects.all()
    if request.POST:
        create = Group.objects.create(name=request.POST['message'])
        for i in request.POST.getlist('browser'):
            create.user.add(int(i))
        messages.success(request, 'Спасибо вы создали группу')
        return redirect('reminders:reminderss', group_idi=int(create.id))
    return render(request, 'reminder/add_group.html', {'profile': profile})


def add_reminders(request, group_id):
    forms = CreateIncome()
    forms = CreateIncome(request.POST or None)
    if forms.is_valid():
        forms = forms.save(commit=False)
        forms.name = request.POST['name']
        forms.text = request.POST['message']
        forms.group = Group.objects.get(pk=int(group_id))
        # create = Reminder.objects.create(name=request.POST['name'], text = request.POST['message'] , group=Group.objects.get(pk=int(group_id)))
        forms.save()
        for i in group.user.all():
            forms.user.add(i.id)
        return redirect('reminders:reminderss', group_idi=group_id)
    return render(request, 'reminder/add_reminder.html', {'forms': forms})


def reminders_page(request, group_idi):
    group_id = int(group_idi)
    return render(request, 'reminder/reminder.html', {'gr_id': group_id})


def del_remind(request, del_id):
    if 1 == 1:
        delete = Reminder.objects.get(pk=del_id)
        group = delete.group
        group.user.remove(request.user)
        return redirect('profiles:profiles')
    return render(request, 'reminder/delete_reminder.html', {})
