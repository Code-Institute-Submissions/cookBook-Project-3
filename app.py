import os 
from flask import Flask, render_template
import pymongo

if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "cookBook"
COLLECTION = "Recipe"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") %e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]


recipes = coll.objects
print(recipes)
#for doc in Recepies:
 #   print(doc)


app = Flask(__name__)


''' List of recipes'''
@app.route("/")
def index():
    return render_template("index.html")



if __name__ =="__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)