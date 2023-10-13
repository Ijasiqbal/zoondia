from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

class CustomLoginView(LoginView):
    template_name = 'login.html'

# Create your views here.
def register(request):  
    if request.method == 'POST':  
        form = UserCreationForm(request.POST)  
        if form.is_valid():  
            user = form.save() 
            login(request, user)
            return redirect('login') 
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

def dashboard(request):
    return render(request,'dashboard.html')
