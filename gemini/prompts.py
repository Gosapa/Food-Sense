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
{{"name": NAME OF THE FOOD, "ingredients": LIST OF THE REQUIRED INGREDIENTS, "steps": STEP-BY-STEP INSTRUCTIONS FOR PREPARING THIS FOOD, MARKDOWN FORMATTED. PLEASE INCLUDE THE STEP NUMBER}}
SAMPLE OUTPUT:
{{"name": "Pan-Seared Beef Steak with Garlic Herb Butter", "ingredients": ["1 (1-inch thick) beef steak (sirloin, ribeye, or New York strip)", "1 tablespoon olive oil", "1 tablespoon unsalted butter", "2 cloves garlic, minced", "1 tablespoon fresh parsley, chopped", "1 teaspoon fresh thyme, chopped", "1/2 teaspoon salt", "1/4 teaspoon black pepper", "Optional: 1 teaspoon Dijon mustard"], "steps": "**1. Prepare the Steak:** Pat the steak dry with paper towels. Season generously with salt and pepper on both sides. Let it rest at room temperature for 15-20 minutes before cooking. This helps the steak cook evenly.   \n2. Heat the Pan:** Heat the olive oil in a heavy-bottomed skillet over medium-high heat. The pan should be smoking hot before adding the steak.   \n3. Sear the Steak:** Place the steak in the hot skillet and sear for 2-3 minutes per side, or until nicely browned. If you want a rare steak, cook for a shorter time; for medium-rare, cook a little longer.    \n4. Create the Garlic Herb Butter:** While the steak is searing, melt the butter in a small saucepan over medium heat. Add the minced garlic, parsley, and thyme. Stir until fragrant, about 30 seconds.    \n5. Finish Cooking:** Transfer the steak to a plate and let it rest for 5-10 minutes. This allows the juices to redistribute, resulting in a more tender and flavorful steak.   \n6. Serve:**  Pour the garlic herb butter over the steak and enjoy!"}}
"""

def p_recommendation(data, profile):
    return f"""
These are the nearby restaurants around me: 
{data}

This is the user's profile information:
age: {profile.age}
height(cm): {profile.height}
weight(kg): {profile.weight}
diseases: {profile.diseases}
allergies: {profile.allergies}

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
{{"name": NAME OF THE FOOD, "ingredients": LIST OF THE REQUIRED INGREDIENTS, "steps": STEP-BY-STEP INSTRUCTIONS FOR PREPARING THIS FOOD, MARKDOWN FORMATTED. PLEASE INCLUDE THE STEP NUMBER}}
SAMPLE OUTPUT:
{{"name": "Pan-Seared Beef Steak with Garlic Herb Butter", "ingredients": ["1 (1-inch thick) beef steak (sirloin, ribeye, or New York strip)", "1 tablespoon olive oil", "1 tablespoon unsalted butter", "2 cloves garlic, minced", "1 tablespoon fresh parsley, chopped", "1 teaspoon fresh thyme, chopped", "1/2 teaspoon salt", "1/4 teaspoon black pepper", "Optional: 1 teaspoon Dijon mustard"], "steps": "**1. Prepare the Steak:** Pat the steak dry with paper towels. Season generously with salt and pepper on both sides. Let it rest at room temperature for 15-20 minutes before cooking. This helps the steak cook evenly.   \n2. Heat the Pan:** Heat the olive oil in a heavy-bottomed skillet over medium-high heat. The pan should be smoking hot before adding the steak.   \n3. Sear the Steak:** Place the steak in the hot skillet and sear for 2-3 minutes per side, or until nicely browned. If you want a rare steak, cook for a shorter time; for medium-rare, cook a little longer.    \n4. Create the Garlic Herb Butter:** While the steak is searing, melt the butter in a small saucepan over medium heat. Add the minced garlic, parsley, and thyme. Stir until fragrant, about 30 seconds.    \n5. Finish Cooking:** Transfer the steak to a plate and let it rest for 5-10 minutes. This allows the juices to redistribute, resulting in a more tender and flavorful steak.   \n6. Serve:**  Pour the garlic herb butter over the steak and enjoy!"}}
"""