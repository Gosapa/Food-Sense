from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Profile, Favorite
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
import json

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
        print(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.diseases = request.POST.getlist('diseases')
            profile.allergies = request.POST.getlist('allergies')
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

@login_required
def save_favorite(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            print(data)
            entry = Favorite()
            entry.user = request.user
            entry.name = data.get('item')
            entry.ingredients = data.get('ingredients')
            entry.steps = data.get('steps')
            entry.save()
            return JsonResponse({'message': 'Recipe saved to favorites!'})

        except Profile.DoesNotExist:
            return JsonResponse({'message': 'Profile not found.'}, status=404)

    return JsonResponse({'message': 'Invalid request method.'}, status=405)



@login_required
def delete_favorite(request):
    if request.method == 'POST':
        favorite_id = request.GET.get('favorite_id')
        try:
            favorite = Favorite.objects.get(pk=favorite_id)
            favorite.delete()
            return JsonResponse({'success': True})
        except Favorite.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'favorite not found.'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method.'})