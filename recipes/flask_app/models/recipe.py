from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.under_30_min = data['under_30_min']
        self.description = data['description']
        self.instructions = data['instructions']
        self.recipe_made = data['recipe_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, under_30_min, description, instructions, recipe_made, created_at, updated_at, user_id) VALUES (%(name)s, %(under_30_min)s, %(description)s, %(instructions)s, %(recipe_made)s, NOW(), NOW(), %(user_id)s);"
        results = connectToMySQL('recipes_schema').query_db(query, data)
        return results

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL('recipes_schema').query_db(query)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL('recipes_schema').query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name = %(name)s, under_30_min = %(under_30_min)s, description = %(description)s, instructions = %(instructions)s, recipe_made = %(recipe_made)s, updated_at = NOW() WHERE id = %(id)s;"
        results = connectToMySQL('recipes_schema').query_db(query, data)
        return results

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL('recipes_schema').query_db(query, data)
        return results

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash("Recipe name must be at least 3 characters!!","create_edit")
            is_valid = False
        if len(recipe["description"]) < 3:
            flash("Recipe description must be at least 3 characters!!","create_edit")
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash("Recipe instructions must be at least 3 characters!!","create_edit")
            is_valid = False
        if recipe['date_made'] == "":
            flash("Please insert a proper date!!","create_edit")
            is_valid = False
        if "under_30_min" not in recipe:
            flash("Please pick 'yes' or 'no' for 'Under 30 minutes?'.","create_edit")
            is_valid = False
        return is_valid