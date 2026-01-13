from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_engine import suggest_recipes
from db import db

# 1️⃣ Create Flask app FIRST
app = Flask(__name__)
CORS(app)

# 🔹 PostgreSQL config
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres123@localhost:5432/smart_recipe_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 🔹 Initialize DB with app
db.init_app(app)

# 2️⃣ Home route
@app.route("/")
def home():
    return "Smart Recipe Finder Backend is running!"

# 3️⃣ Recipe suggestion route
@app.route("/suggest-recipes", methods=["POST"])
def suggest():
    data = request.json
    ingredients = data.get("ingredients", [])

    recipes = suggest_recipes(ingredients)
    return jsonify(recipes)

# 4️⃣ Run server
if __name__ == "__main__":
    app.run(debug=True)
