from . import config, prompts


def generate_recipe(item, profile):
    model = config.recipe_model
    prompt = prompts.p_recipe(item, profile)
    print(prompt)
    chat = model.start_chat()
    response = chat.send_message(prompt)
    print(response.text)
    return response.text

def generate_recommendation(data):
    model = config.recommendation_model
    prompt = prompts.p_recommendation(data)
    print(prompt)
    chat = model.start_chat()
    response = chat.send_message(prompt)
    print(response.text)
    return response.text

def generate_ingredient_recipe(ingredients, profile):
    model = config.ingredient_recipe_model
    prompt = prompts.p_ingredient_recipe(ingredients, profile)
    print(prompt)
    chat = model.start_chat()
    response = chat.send_message(prompt)
    print(response.text)
    return response.text