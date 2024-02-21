from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm
from .models import Profile

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data 
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Account disabled')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})

def user_logout(request):
    # Logout the user
    logout(request)
    # Redirect to a template or another view after logout
    return render(request, 'account/logged_out.html')

@login_required(login_url='/account/login/')
def dashboard(request):
    return render(request, 'account/dashboard.html')


        
