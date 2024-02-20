from django.shortcuts import render, redirect
from .models import Profile
from django.contrib import messages

# Create your views here.

def dashboard(request):
    return render(request, "dashboard.html", {})

def profile_list(request):
    
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {"profiles":profiles})
    else:
        messages.success(request, ("You must be logged in to use that page"))
        return redirect('dashboard')
    
def profile(request, pk):

    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        return render(request, "profile.html", {"profile":profile})
    else:
        messages.success(request, ("You must be logged in to use that page"))
        return redirect('dashboard')