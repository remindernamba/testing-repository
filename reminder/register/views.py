from django.shortcuts import render
from register.forms import UserRegistration
from django.contrib import auth
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.


def register(request):
    user = UserRegistration(request.POST)
    print request.POST
    if user.is_valid():
        save = user.save(commit=False)
        save.set_password(user.cleaned_data['password'])
        save.save()
        return redirect('/')
    return render(request, 'register/register.html', {'forms': user})


def authentication(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        messages.success(request, 'You have Authenticated')
        auth.login(request, user)
        return redirect('/')
    return render(request, 'register/login.html',)
