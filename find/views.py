from .markdownRenderer import md_to_html
from django.shortcuts import render, redirect
from django.http import JsonResponse
import googlemaps
from gemini.functions import *
from django.contrib.auth.decorators import login_required
from foodapp.settings import GOOGLE_API_KEY, GOOGLE_AI_KEY
import requests
from users.models import Profile, Favorite
import json
import google.generativeai as genai

gmaps = googlemaps.Client(key=GOOGLE_API_KEY)
genai.configure(api_key=GOOGLE_AI_KEY)

# Create your views here.


def index(request):
    return render(request, "find/index.html")

@login_required
def find(request):
    if request.method == "POST":

        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")
        url = "https://places.googleapis.com/v1/places:searchNearby"
        myHeader = {
            'Content-Type': 'application/json',
            'X-Goog-Api-Key': GOOGLE_API_KEY,
            'X-Goog-FieldMask': 'places.displayName,places.id,places.types,places.formattedAddress'
        }
        myBody = {
            'includedTypes': ['restaurant'],
            'maxResultCount': 10,
            'locationRestriction': {
                'circle': {
                    'center': {
                        'latitude': latitude,
                        'longitude': longitude,
                    },
                    'radius': 2000.0
                }
            },
            'rankPreference': 'DISTANCE'
        }

        result = requests.post(url, json=myBody, headers=myHeader).json()
        # print(type(result)) // DICTIONARY
        # print(result)
        places = []
        for restaurant in result['places']:
            new_data = {
                'displayName': restaurant['displayName']['text'],
                'address': restaurant['formattedAddress'],
                'types':  restaurant['types'],
            }
            places.append(new_data)
            
            # print(f"Name: {restaurant['displayName']['text']}")
            # print(f"Address: {restaurant['formattedAddress']}")
            # print(f"Types: {restaurant['types']}")
            # print("-" * 20)

        context = {
            "latitude": latitude,
            "longitude": longitude,
            "places": places,
        }
        return render(request, "find/find.html", context)
        # nearby_restaurants = gmaps.places_nearby(
        #     location=(latitude, longitude),
        #     radius = 5000,
        #     type = 'restaurant',
        #     rankby = 'distance',
        # )
        # print(nearby_restaurants)
        # nearby_restaurants = gmaps.places.textsearch(
        #     query='restaurants',  # Search for restaurants (can be more specific)
        #     location=(latitude, longitude),  # Your location
        #     radius=5000,  # Search within a 5 km radius
        #     rankby='distance',  # Sort by distance
        # )
        # for restaurant in nearby_restaurants['results']:
        #     print(f"Name: {restaurant['name']}")
        #     print(f"Address: {restaurant['vicinity']}")
        #     print(f"Types: {restaurant['types']}")
        #     print("-" * 20)
    else:
        return redirect('index')
    
@login_required
def generate(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        response = generate_recommendation(data)
        return JsonResponse({'response': md_to_html(response)}, safe=False)
    else:
        return JsonResponse({'message': 'Invalid request Method'}, status=400)

@login_required
def recipe(request):
    try:
        profile = Profile.objects.get(user=request.user)
        return render(request, 'find/recipe.html')
    except Profile.DoesNotExist:
        return redirect('users:createProfile')

@login_required
def generateRecipe(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        data = json.loads(request.body)
        item = data['item']
        response = json.loads(generate_recipe(item, profile))
        # response['steps'] = md_to_html(response['steps'])
        return JsonResponse({"response": response})
    else:
        return JsonResponse({"message": "Invalid request method"}, status=400)
    

@login_required
def findIngredient(request):
    try:
        profile = Profile.objects.get(user=request.user)
        return render(request, "find/ingredients.html")
    except Profile.DoesNotExist:
        return redirect('users:createProfile')

@login_required
def ingredientRecipe(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        data = json.loads(request.body)
        ingredients = data['ingredients']
        response = json.loads(generate_ingredient_recipe(ingredients, profile))
        # response['steps'] = md_to_html(response['steps'])
        
        return JsonResponse({"response": response}, safe=False)
    else:
        return JsonResponse({"message": "Invalid request method"}, status=400)