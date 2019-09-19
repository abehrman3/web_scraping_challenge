from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_news
import scrape_image
import scrape_weather


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/space_app"

mongo = PyMongo(app)


@app.route("/")
def home():

    space_data = mongo.db.mars_db.find_one()
    image_data = mongo.db.news_db.find_one()
    weather_mars = mongo.db.weather_db.find_one()

    return render_template("index.html", planet=space_data, galaxy=image_data, weather=weather_mars)


@app.route("/scrape")
def scrape():
    mars_db = mongo.db.mars_db
    news_db = mongo.db.news_db
    weather_db = mongo.db.weather_db

    nasa_news = scrape_news.scrape_news()
    nasa_image = scrape_image.scrape_image()
    weather_data = scrape_weather.scrape_weather()


    mars_db.update({}, nasa_news, upsert=True)
    news_db.update({}, nasa_image, upsert=True)
    weather_db.update({}, weather_data, upsert=True)


    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
