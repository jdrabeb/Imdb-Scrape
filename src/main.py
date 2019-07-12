from videogame import Videogame
from imdbScrape import imdbScrape
from app import db

URL = 'https://www.imdb.com/search/title/?genres=drama&sort=user_rating&title_type=game'
DATA_LIMIT = 10

games = imdbScrape.scrape_games(URL, DATA_LIMIT)
#imdbScrape.create_csv(games)

db.create_all()
for game in games:
    db.session.add(game)
    db.session.commit()
