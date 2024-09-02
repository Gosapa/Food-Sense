from users.models import Profile

def p_recipe(item, profile):
    return f"""
Hello!
Can you tell me detailed ingredients, steps, and tips for making {item}?

This is the user's profile information:
age: {profile.age}
height(cm): {profile.height}
weight(kg): {profile.weight}
diseases: {profile.diseases}
allergies: {profile.allergies}

Please consider the user's information, such as allergies and diseases in creating the recipe. 
For example, when user wants to create a recipe containing peanut but has peanut allergy, give an alternative to the user.
For example, when user has diabetes in his diseases, please consider giving the user a recipe with balanced nutrients with low carb and low cholestrol. 

OUTPUT FORMAT:
{{"name": NAME OF THE FOOD, "description": DESCRIPTION OF THE FOOD, "ingredients": LIST OF THE REQUIRED INGREDIENTS, "steps": STEP-BY-STEP INSTRUCTIONS FOR PREPARING THIS FOOD, HTML FORMAT. PLEASE INCLUDE THE STEP NUMBER}}
EXAMPLE OUTPUT:
{{"name": "Chocolate Peanut Butter Protein Balls", "description": "These no-bake protein balls are a delicious and healthy snack option. They're packed with protein, fiber, and healthy fats, making them a great way to satisfy your sweet tooth without sacrificing your health goals. While peanut butter is a traditional ingredient, I understand your allergy. This recipe offers alternatives like sunflower seed butter or tahini to create a delicious and allergy-friendly treat.", "ingredients": ["1/2 cup chocolate chips", "1/4 cup peanut butter (or substitute with sunflower seed butter, tahini, or almond butter)", "1/4 cup rolled oats", "1/4 cup protein powder (vanilla or chocolate flavored)", "1/4 cup honey", "1/4 cup shredded coconut (optional)", "1/4 teaspoon vanilla extract", "Pinch of salt"], "steps": "<ol>\n<li>\n<p><strong>Melt the chocolate:</strong> In a microwave-safe bowl, melt the chocolate chips in 30-second intervals, stirring after each interval, until smooth. If using a double boiler, heat the chocolate slowly over simmering water.</p>\n</li>\n<li>\n<p><strong>Combine ingredients:</strong> In a large bowl, combine the melted chocolate, peanut butter (or substitute), rolled oats, protein powder, honey, coconut (if using), vanilla extract, and salt. Mix well until everything is combined and a dough forms.</p>\n</li>\n<li>\n<p><strong>Shape the balls:</strong> Using your hands, roll the mixture into bite-sized balls. Place the balls on a baking sheet lined with parchment paper.</p>\n</li>\n<li>\n<p><strong>Chill and serve:</strong> Refrigerate the protein balls for at least 30 minutes to allow them to firm up. Enjoy as a healthy snack or dessert!</p>\n</li>\n</ol>"}}
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

Please consider the user's information, such as allergies and diseases in creating the recipe. 
For example, when user wants to create a recipe containing peanut but has peanut allergy, give an alternative to the user.
For example, when user has diabetes in his diseases, please consider giving the user a recipe with balanced nutrients with low carb and low cholestrol. 
What food can I make with these ingredients? You can be creative as well! You can also include simple ingredients that are not provided by the user, such as salt or pepper. 

OUTPUT FORMAT:
{{"name": NAME OF THE FOOD, "description": DESCRIPTION OF THE FOOD, "ingredients": LIST OF THE REQUIRED INGREDIENTS, "steps": STEP-BY-STEP INSTRUCTIONS FOR PREPARING THIS FOOD, HTML FORMAT. PLEASE INCLUDE THE STEP NUMBER}}
EXAMPLE OUTPUT:
{{"name": "Chocolate Peanut Butter Protein Balls", "description": "These no-bake protein balls are a delicious and healthy snack option. They're packed with protein, fiber, and healthy fats, making them a great way to satisfy your sweet tooth without sacrificing your health goals. While peanut butter is a traditional ingredient, I understand your allergy. This recipe offers alternatives like sunflower seed butter or tahini to create a delicious and allergy-friendly treat.", "ingredients": ["1/2 cup chocolate chips", "1/4 cup peanut butter (or substitute with sunflower seed butter, tahini, or almond butter)", "1/4 cup rolled oats", "1/4 cup protein powder (vanilla or chocolate flavored)", "1/4 cup honey", "1/4 cup shredded coconut (optional)", "1/4 teaspoon vanilla extract", "Pinch of salt"], "steps": "<ol>\n<li>\n<p><strong>Melt the chocolate:</strong> In a microwave-safe bowl, melt the chocolate chips in 30-second intervals, stirring after each interval, until smooth. If using a double boiler, heat the chocolate slowly over simmering water.</p>\n</li>\n<li>\n<p><strong>Combine ingredients:</strong> In a large bowl, combine the melted chocolate, peanut butter (or substitute), rolled oats, protein powder, honey, coconut (if using), vanilla extract, and salt. Mix well until everything is combined and a dough forms.</p>\n</li>\n<li>\n<p><strong>Shape the balls:</strong> Using your hands, roll the mixture into bite-sized balls. Place the balls on a baking sheet lined with parchment paper.</p>\n</li>\n<li>\n<p><strong>Chill and serve:</strong> Refrigerate the protein balls for at least 30 minutes to allow them to firm up. Enjoy as a healthy snack or dessert!</p>\n</li>\n</ol>"}}
"""