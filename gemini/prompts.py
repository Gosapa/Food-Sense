from users.models import Profile

def p_recipe(item, profile):
    return f"""
Hello!
Can you tell me detailed ingredients, steps, and tips for making {item}.

This is the user's profile information:
age: {profile.age}
height(cm): {profile.height}
weight(kg): {profile.weight}
diseases: {profile.diseases}
allergies: {profile.allergies}

OUTPUT FORMAT:
{{"name": NAME OF THE FOOD, "ingredients": LIST OF THE REQUIRED INGREDIENTS, "steps": STEP-BY-STEP INSTRUCTIONS FOR PREPARING THIS FOOD, HTML FORMAT. PLEASE INCLUDE THE STEP NUMBER}}
EXAMPLE OUTPUT:
{{"name": "Kimchi Jjigae (Kimchi Stew)", "ingredients": ["1 cup cooked kimchi (rinsed to reduce spiciness)", "1/2 cup diced tofu", "1/4 cup chopped onion", "1/4 cup chopped green onion", "2 cloves garlic, minced", "1 teaspoon gochugaru (Korean chili powder)", "1 teaspoon soy sauce", "1 tablespoon gochujang (Korean chili paste)", "1 cup dashi (or water)", "1 teaspoon sugar", "1/4 cup chopped scallions", "Optional: 1/2 cup sliced mushrooms", "Optional: 1/2 cup cooked pork belly"], "steps": "<ol>\n<li>\n<p><strong>Prepare the kimchi:</strong> If using pre-made kimchi, rinse it well to reduce spiciness. If making your own kimchi, let it ferment for at least a week before using.</p>\n</li>\n<li>\n<p><strong>Sauté the aromatics:</strong> In a large pot or Dutch oven, heat a tablespoon of oil over medium heat. Add the chopped onion and minced garlic, and sauté until fragrant, about 2 minutes.</p>\n</li>\n<li>\n<p><strong>Add kimchi and spices:</strong> Stir in the rinsed kimchi, gochugaru, gochujang, soy sauce, and sugar. Cook for 5 minutes, stirring occasionally, to allow the flavors to meld.</p>\n</li>\n<li>\n<p><strong>Add dashi and tofu:</strong> Pour in the dashi (or water) and bring to a simmer. Add the diced tofu and chopped green onion.</p>\n</li>\n<li>\n<p><strong>Simmer and serve:</strong> Reduce the heat to low and simmer for 15 minutes, or until the tofu is heated through and the flavors have combined. Adjust the seasoning to taste. Before serving, garnish with chopped scallions and optional additions like mushrooms and pork belly.</p>\n</li>\n</ol>"}}
"""

def p_recommendation(data):
    return f"""
These are the nearby restaurants around me: 
{data}


Can you tell me about each of these restaurants based on the data that you provided, mainly using the name? And then, simply recommend 1 restaurant. Please convert all utf-16 encoded korean characters accordingly, and use the same name as the restaurants without romanizing them.
    """

def p_ingredient_recipe(ingredients, profile):
    return f"""
These are the ingredients I currently have!
{ingredients}

This is the user's profile information:
age: {profile.age}
height(cm): {profile.height}
weight(kg): {profile.weight}
diseases: {profile.diseases}
allergies: {profile.allergies}

What food can I make with these ingredients? You can be creative as well! You can also include simple ingredients that are not provided by the user, such as salt or pepper. 

OUTPUT FORMAT:
{{"name": NAME OF THE FOOD, "ingredients": LIST OF THE REQUIRED INGREDIENTS, "steps": STEP-BY-STEP INSTRUCTIONS FOR PREPARING THIS FOOD, HTML FORMAT. PLEASE INCLUDE THE STEP NUMBER}}
EXAMPLE OUTPUT:
{{"name": "Kimchi Jjigae (Kimchi Stew)", "ingredients": ["1 cup cooked kimchi (rinsed to reduce spiciness)", "1/2 cup diced tofu", "1/4 cup chopped onion", "1/4 cup chopped green onion", "2 cloves garlic, minced", "1 teaspoon gochugaru (Korean chili powder)", "1 teaspoon soy sauce", "1 tablespoon gochujang (Korean chili paste)", "1 cup dashi (or water)", "1 teaspoon sugar", "1/4 cup chopped scallions", "Optional: 1/2 cup sliced mushrooms", "Optional: 1/2 cup cooked pork belly"], "steps": "<ol>\n<li>\n<p><strong>Prepare the kimchi:</strong> If using pre-made kimchi, rinse it well to reduce spiciness. If making your own kimchi, let it ferment for at least a week before using.</p>\n</li>\n<li>\n<p><strong>Sauté the aromatics:</strong> In a large pot or Dutch oven, heat a tablespoon of oil over medium heat. Add the chopped onion and minced garlic, and sauté until fragrant, about 2 minutes.</p>\n</li>\n<li>\n<p><strong>Add kimchi and spices:</strong> Stir in the rinsed kimchi, gochugaru, gochujang, soy sauce, and sugar. Cook for 5 minutes, stirring occasionally, to allow the flavors to meld.</p>\n</li>\n<li>\n<p><strong>Add dashi and tofu:</strong> Pour in the dashi (or water) and bring to a simmer. Add the diced tofu and chopped green onion.</p>\n</li>\n<li>\n<p><strong>Simmer and serve:</strong> Reduce the heat to low and simmer for 15 minutes, or until the tofu is heated through and the flavors have combined. Adjust the seasoning to taste. Before serving, garnish with chopped scallions and optional additions like mushrooms and pork belly.</p>\n</li>\n</ol>"}}
"""