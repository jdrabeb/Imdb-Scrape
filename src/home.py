from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import redirect
from flask import jsonify
from imdbScrape import imdbScrape
from app import create_app
from videogame import Videogame
from serializer import create_csv, create_json
from timed import timed

URL = 'https://www.imdb.com/search/title/?genres=drama&sort=user_rating&title_type=game'
DATA_LIMIT = 20

db, app = create_app()

scrape_games = imdbScrape.scrape_games(URL, DATA_LIMIT)
for game in scrape_games:
    db.session.add(game)
    db.session.commit()

# Save games added to database in a csv file
create_csv(scrape_games)
# Save games added to database in a json file
#create_json(scrape_games)

'''
Home page of the app
Displays all the video games in the database
'''
@timed(enabled=True)
@app.route("/", methods=["GET", "POST"])
def home():
    games = Videogame.query.all()
    return render_template("index.html", games = games)

'''
Search a video game by substring in the title
The results are displayed on the index page
'''
@timed(enabled=True)
@app.route("/search", methods=["GET", "POST"])
def search():
    search_title = request.form.get("search_title")
    found_games = Videogame.query.filter(
            Videogame.title.contains(search_title)).all()
    return render_template("index.html", games = found_games)

'''
Add a video game to the database
'''
@timed(enabled=True)
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

'''
Update the genre of a given video game
'''
@timed(enabled=True)
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

'''
Delete a given video game from the database
the game is also deleted from the display
'''
@timed(enabled=True)
@app.route("/delete", methods=["POST"])
def delete():
    # Delete a video game from the database by id
    game_id = request.form.get("game_id")
    Videogame.query.filter_by(game_id=game_id).delete()
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
