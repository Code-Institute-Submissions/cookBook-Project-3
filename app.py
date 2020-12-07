import os 
import json
from flask import (
        Flask, flash, render_template, 
        redirect, request, session, url_for, jsonify)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime,timedelta
import pymongo
from datetime import datetime, timedelta
import json

if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


''' List of recipes'''

@app.route("/")
def recipe():
    recipes = mongo.db.Recipe.find()
    print(recipes)
    return render_template("index.html", recipes=recipes)


''' Search for specific recipes'''
@app.route("/search", methods=["GET","POST"])
def search():
        query = request.form.get("querySearch")
        recipes = mongo.db.Recipe.find({"$text":{"$search":query}})
        return render_template("index.html", recipes=recipes)
   

''' Add  recipes'''
@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        #Adding a new recipe variables
        recipe = {
            "dish": request.form.get("dishName"),
            "cuisine": request.form.get("cuisine"),
            "course": request.form.get("course"),
            "required_tool": request.form.get("required_tools"),
            "ingredients": request.form.get("ingredients"),
            "instructions": request.form.get("instructions"),
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
         #Adding a new recipe to db
        mongo.db.Recipe.insert_one(recipe)
        flash("Success!! The new was recipe added")
        return redirect(url_for("recipe"))
    else:
        #go to add page
        return render_template("add.html")


''' Update specific recipes'''
@app.route("/update/<recipe_id>", methods = ["GET","POST"])
def update(recipe_id):
    if request.method =="POST":
        submit = {
            "dish": request.form.get("dishName"),
            "cuisine": request.form.get("cuisine"),
            "course": request.form.get("course"),
            "required_tool": request.form.get("required_tools"),
            "ingredients": request.form.get("ingredients"),
            "instructions": request.form.get("instructions"),
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
         #Adding a new recipe to db
        mongo.db.Recipe.update({"_id":ObjectId(recipe_id)},submit)
        flash("Success!! The recipe was updated!")
        return redirect(url_for('recipe'))
                
    recipe = mongo.db.Recipe.find_one({"_id": ObjectId(recipe_id)})
    return render_template("update.html",recipe = recipe)


''' View/Display specific recipes'''
@app.route("/view/<recipe_id>", methods = ["GET","POST"])
def view(recipe_id):
    recipe = mongo.db.Recipe.find_one({"_id": ObjectId(recipe_id)})
    return render_template("view.html",recipe = recipe)


''' Remove  specific recipes'''
@app.route("/remove")
def remove():
    recipe_id = request.args.get('id')
    print(recipe_id)
    recipe = mongo.db.Recipe.remove({"_id": ObjectId(recipe_id)})
    flash("Success!! The recipe was deleted")
    return jsonify({'response':'success'})
    


if __name__ =="__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=False)