from django.template import Template, Context
from django.template.defaultfilters import safe
from django.shortcuts import render, redirect
from django.http import JsonResponse
import googlemaps
from foodapp.settings import GOOGLE_API_KEY, GOOGLE_AI_KEY
import requests
import json
import google.generativeai as genai

gmaps = googlemaps.Client(key=GOOGLE_API_KEY)
genai.configure(api_key=GOOGLE_AI_KEY)

# Create your views here.

def index(request):
    return render(request, "find/index.html")

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
            'maxResultCount': 5,
            'locationRestriction': {
                'circle': {
                    'center': {
                        'latitude': latitude,
                        'longitude': longitude,
                    },
                    'radius': 500.0
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
            # add code here!
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
    
def generate(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        data_string = json.dumps(data)
        # print(data_string)
        model = genai.GenerativeModel(
            model_name = "gemini-1.5-pro-latest",
            system_instruction="You are a restaurant recommender AI, who gives detailed explanation of restaurants and its benefits, even with limited information. You should show confidence to users, so do not apologize to the user with possible mistakes. "
        )
        chat = model.start_chat()

        response = chat.send_message(
            "These are the nearby restaurants around me: " +
            data_string +
            "Can you tell me about each of these restaurants based on the data that you provided, mainly using the name? And then, simply recommend 1 restaurant. Please convert all utf-16 encoded korean characters accordingly."
        )
        response_text = response.text
        template = Template("{{ response_text | markdown | safe}}")
        # print(response.text)
        context = Context({'response_text': response_text})
        response_html = template.render(context)
        # print(response_html)
        return JsonResponse({'response': response_html}, safe=False)
    else:
        return JsonResponse({'message': 'Invalid Resposne Method'})

def recipe(request):
    return render(request, 'find/recipe.html')