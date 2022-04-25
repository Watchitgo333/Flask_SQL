
from operator import methodcaller
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.recipe import Recipe
# from flask_app.controllers import users

@app.route('/recipes/new')
def new_recipe():
    if "user_id" not in session:
        return redirect("/")
    # print(session['user_id'])
    return render_template('new_recipe.html')

@app.route('/create_recipe', methods=['post'])
def create_recipe():
    data = {
        "name" : request.form['name'],
        "description" : request.form['description'],
        "instructions" : request.form['instructions'],
        "recipe_made" : request.form['date_made'],
        "under_30_min" : request.form['under_30'],
        "user_id" : session["user_id"]
    }
    Recipe.save(data)
    return redirect('/dashboard')

@app.route('/delete_recipe')
def delete_recipe():
    if "user_id" not in session:
        return redirect('/')
    data = {
        "id" : session['user_id']
    }
    Recipe.delete(data)
    return redirect('/dashboard')

@app.route('/edit_recipe/<int:id>')
def edit_recipe_page(id):
    if "user_id" not in session:
        return redirect('/')
    data = {
        "id" : id
    }
    recipe = Recipe.get_one(data)
    print(recipe.under_30_min == "no")
    return render_template("edit_recipe.html", one_recipe = recipe)

@app.route('/view/<int:id>')
def view_recipe(id):
    if "user_id" not in session:
        return redirect('/')
    data = {
        "id" : id
    }
    recipe = Recipe.get_one(data)
    return render_template("view.html", one_recipe = recipe)

@app.route('/edit_recipe/<int:id>', methods=['post'])
def edit_recipe(id):
    recipe_id = {
        "id" : id
    }
    recipe = Recipe.get_one(recipe_id)
    if not Recipe.validate_recipe(request.form):
        return redirect(f'/edit_recipe/{recipe.id}')
    data = {
        "name" : request.form['name'],
        "description" : request.form['description'],
        "instructions" : request.form['instructions'],
        "recipe_made" : request.form['date_made'],
        "under_30_min" : request.form['under_30_min'],
        "id" : id
    }
    Recipe.update(data)
    return redirect('/dashboard')