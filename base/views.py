from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

def index(request):
    """Placeholder index view"""
    return render(request, 'index.html')
    
def login_view(request):
    """Placeholder index view"""
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    print(request.session.keys())
    return redirect('home')
    #return render(request, 'logout.html')
    
    
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)    
def logged_in_view(request):
    user = request.user
    username = request.user.username
    context = {'username': username}
    return render(request, 'logged_in.html', context)

