from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from Home.models import User


def main_page(request):
    return render(request, 'base.html')

def register(request):
    return render(request, 'registration/register.html')

def main_logged_in(request):

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            HttpRedirect
            #Redirect to a success page.
        else:
            # Return a 'disabled account' error message
            ...
    else:
        # Return an 'invalid login' error message.
        ...
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    # Redirect to a success page.




