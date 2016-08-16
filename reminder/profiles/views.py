from django.shortcuts import render
from note.models import Reminder, Group

def index(request):
    return render(request, 'main/index.html', {})
