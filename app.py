import os 
from flask import (
        Flask, flash, render_template, 
        redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import pymongo
from datetime import datetime, timedelta

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


@app.route("/search", methods=["GET","POST"])
def search():
        query = request.form.get("querySearch")
        recipes = mongo.db.Recipe.find({"$text":{"$search":query}})
        return render_template("index.html", recipes=recipes)
   

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
        flash("New recipe added")
        return redirect(url_for("recipe"))
        flash("New recipe added")
    else:
        #go to add page
        return render_template("add.html")


if __name__ =="__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)