import google.generativeai as genai
from foodapp.settings import GOOGLE_AI_KEY

genai.configure(api_key=GOOGLE_AI_KEY)

recipe_model = genai.GenerativeModel("gemini-1.5-flash",
                                    system_instruction="You are a excellent chef who can explain good, affordable recipes to people in a kindly manner.",
                                    generation_config={"response_mime_type": "application/json"})
recommendation_model = genai.GenerativeModel("gemini-1.5-flash-latest",
                                             system_instruction="You are a restaurant recommender AI, who gives detailed explanation of restaurants and its benefits, even with limited information. You should show confidence to users, so do not apologize to the user with possible mistakes.")

ingredient_recipe_model = genai.GenerativeModel("gemini-1.5-flash-latest",
                                             system_instruction="You are an expert chef who specializes in creating recipe with affordable ingredients. You are tasked with giving a detailed recipe for a client, who will tell you about what ingredients they have. Please provide them with detailed guide, and be friendly!",
                                             generation_config={"response_mime_type": "application/json"})