from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
from imdbScrape import imdbScrape
from app import create_app
from videogame import Videogame

URL = 'https://www.imdb.com/search/title/?genres=drama&sort=user_rating&title_type=game'
DATA_LIMIT = 10

db, app = create_app()

@app.route("/", methods=["GET", "POST"])
def home():
    # Add scraped data to the database
    scrape_games = imdbScrape.scrape_games(URL, DATA_LIMIT)
    for game in scrape_games:
        db.session.add(game)
        db.session.commit()

    return render_template("index.html", games = Videogame.query.all())

if __name__ == "__main__":
    app.run(debug=True)
