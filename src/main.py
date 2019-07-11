from videogame import Videogame
from imdbScrape import imdbScrape

url = 'https://www.imdb.com/search/title/?genres=drama&sort=user_rating&title_type=game'
games = imdbScrape.scrape_games(url)
print(games)
