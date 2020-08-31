from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/mar_app")

@app.route("/")
def home():
    mars_data = mongo.db.mars.find_one()
    return render_template("index.html",data=mars_data)

@app.route("/scrape")
def scrape():
    mars_data = mongo.db.mars
    new_info = scrape_mars.scrape()
    mars_data.update({}, new_info, upsert=True)
    return redirect("/", code=302)



if __name__ == "__main__":
    app.run(debug=True)





