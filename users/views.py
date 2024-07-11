from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def profile(request):
    try:
        userProfile = Profile.objects.get(user=request.user)
        print(userProfile)
        return render(request, 'users/profile.html', {'profile': userProfile})
    except Profile.DoesNotExist:
        return render(request, 'users/redirect.html')

@login_required
def create(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        profile = form.save(commit=False)
        profile.user = request.user
        profile.save()
        return redirect('profile')
    return render(request, 'users/profileform.html', {'form':form})