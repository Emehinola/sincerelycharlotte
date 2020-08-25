from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . forms import RegistrationForm

# Create your views here.

#user login view
def login_request(request):
    error = "Fill in your login details correctly"
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = 'incorrrect email or password. Try again'

    context = {
        'error': error
        }

    return render(request, 'user/login.html', context)

def logout_request(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(request, username=request.POST['email'], password=request.POST['password1'])
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    
    context = {
        'form': form,
        'title': 'Registration form'
    }
    return render(request, 'user/registration.html', context)