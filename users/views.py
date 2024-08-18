from django.shortcuts import render, redirect
from .models import Profile, Favorite
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
        return redirect('users:createProfile')

def create(request): 
    if request.method == 'POST':
        print(request.POST)
        print(request.body)
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.diseases = [
                disease for disease in request.POST.getlist('diseases') if disease
            ]
            profile.allergies = [
                allergy for allergy in request.POST.getlist('allergies') if allergy
            ]
            # profile.favorites = [
            #     favorite for favorite in request.POST.getlist('favorites') if favorite
            # ]
            profile.save()
            return redirect('users:profile')
    else:
        form = ProfileForm()
        predefined_diseases = ["Diabetes", "Asthma", "Celiac Disease", "Hypertension"]  # Example
        predefined_allergies = ["Peanut", "Dairy", "Seafood", "Shellfish"]  # Example
        return render(request, 'users/profileform.html', {'form': form,
                                                  'predefined_diseases': predefined_diseases,
                                                  'predefined_allergies': predefined_allergies,})


@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.diseases = [
                disease for disease in request.POST.getlist('diseases') if disease
            ]
            profile.allergies = [
                allergy for allergy in request.POST.getlist('allergies') if allergy
            ]
            # profile.favorites = [
            #     favorite for favorite in request.POST.getlist('favorites') if favorite
            # ]
            profile.save()
            return redirect('users:profile') 
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'users/edit_profile.html', {'form': form, 'profile': profile})

@login_required
def favorites_list(request):
    return render(request, 'users/favorite_list.html')

@login_required
def favorite(request, id):
    item = Favorite.objects.get(id=id)
    return render(request, 'users/favorite.html', {"item": item})