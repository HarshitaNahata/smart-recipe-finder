from models import Recipe

def suggest_recipes(user_ingredients):
    suggestions = []

    # Fetch recipes from DB
    recipes = Recipe.query.all()

    for recipe in recipes:
        recipe_ingredients = [
            i.strip().lower() for i in recipe.ingredients.split(",")
        ]

        match_count = len(
            set(user_ingredients).intersection(recipe_ingredients)
        )

        if match_count > 0:
            suggestions.append({
                "id": recipe.id,
                "title": recipe.title,
                "ingredients": recipe.ingredients,
                "steps": recipe.steps,
                "match_score": match_count
            })

    suggestions.sort(key=lambda x: x["match_score"], reverse=True)
    return suggestions
