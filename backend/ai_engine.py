RECIPES = [
    {
        "name": "Tomato Omelette",
        "ingredients": ["tomato", "egg", "onion"],
        "steps": "Beat eggs, add tomato & onion, cook on pan."
    },
    {
        "name": "Onion Egg Bhurji",
        "ingredients": ["egg", "onion", "oil"],
        "steps": "Cook onion, add eggs, scramble well."
    }
]

def suggest_recipes(user_ingredients):
    suggestions = []

    for recipe in RECIPES:
        match_count = len(
            set(user_ingredients).intersection(recipe["ingredients"])
        )

        if match_count > 0:
            recipe["match_score"] = match_count
            suggestions.append(recipe)

    suggestions.sort(key=lambda x: x["match_score"], reverse=True)
    return suggestions
