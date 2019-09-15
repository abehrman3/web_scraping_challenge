from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_news
import scrape_image
import scrape_weather

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/space_app")


@app.route("/")
def home():

    space_data = mongo.db.collection.find_one()

    return render_template("index.html", planet=space_data)


@app.route("/scrape")
def scrape():

    mars_news = scrape_news.scrape_news()
    mars_image = scrape_image.scrape_image()
    mars_weather = scrape_weather.scrape_weather()

    mongo.db.collection.update({}, mars_news, upsert=True)
    mongo.db.collection.update({}, mars_image, upsert=True)
    mongo.db.collection.update({}, mars_weather, upsert=True)


    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
