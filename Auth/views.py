from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserForm
from Profile.models import Profile

# Create your views here.

def Login(request) : 
    if request.user.is_authenticated : 
        return redirect("home")
    
    if request.method == "POST" : 
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email= email, password= password)

        if user is not None : 
            login(request, user)
            return redirect('home')
        
    return render(request, "Auth/login.html")


def Logout(request) : 
    logout(request)
    return redirect('login')

def Register(request) : 
    if request.user.is_authenticated : 
        return redirect('home')
    
    form = UserForm() 

    if request.method == "POST" : 
        form = UserForm(request.POST)
        if form.is_valid() : 
            form.save()

            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')


            user = authenticate(request= request, email= email, password= password)

            if user is not None : 
                login(request, user)

                profile = Profile.objects.create()
                profile.user = request.user 
                profile.follows.set([user.profile.id])
                profile.save()

                return redirect('edit-profile')
            
    context = {'form': form}
    return render(request, "Auth/register.html", context)