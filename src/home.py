from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import redirect
from imdbScrape import imdbScrape
from app import create_app
from videogame import Videogame

URL = 'https://www.imdb.com/search/title/?genres=drama&sort=user_rating&title_type=game'
DATA_LIMIT = 10

db, app = create_app()

scrape_games = imdbScrape.scrape_games(URL, DATA_LIMIT)
for game in scrape_games:
    db.session.add(game)
    db.session.commit()

@app.route("/", methods=["GET", "POST"])
def home():
    games = Videogame.query.all()
    for game in games:
        print(game.title)
    # Add scraped data to the database
    return render_template("index.html", games = Videogame.query.all())

@app.route("/add", methods=["GET", "POST"])
def add():
    title = request.form.get("title")
    link = request.form.get("link")
    image = request.form.get("image")
    genre = request.form.get("genre")
    date = request.form.get("date")
    rating = request.form.get("rating")
    description = request.form.get("description")
    votes = request.form.get("votes")
    new_game = Videogame(title=title, link=link, image=image, genre=genre,
            date=date, rating=rating, description=description, votes=votes)
    db.session.add(new_game)
    db.session.commit()
    return redirect("/")


@app.route("/update", methods=["POST"])
def update():
    # Update the genre of a given video game in the database
    try:
        new_genre = request.form.get("new_genre")
        old_genre = request.form.get("old_genre")
        game_id = request.form.get("game_id")
        game = Videogame.query.filter_by(game_id=game_id).first()
        game.genre = new_genre
        db.session.commit()
    except Exception as e:
        print(e)
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    # Delete a video game from the database by id
    game_id = request.form.get("game_id")
    Videogame.query.filter_by(game_id=game_id).delete()
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
