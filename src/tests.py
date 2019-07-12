from videogame import Videogame
from imdbScrape import imdbScrape
from serializer import create_json

URL = 'https://www.imdb.com/search/title/?genres=drama&sort=user_rating&title_type=game'
DATA_LIMIT = 10

games = imdbScrape.scrape_games(URL, DATA_LIMIT)
# test create a JSON file
create_json(games)

# test scraping the miniature poster a given game
poster = imdbScrape.scrape_poster_by_title(URL, DATA_LIMIT, "The last of us")
print("The link to the poster of the last of us:")
print(poster)
print()

# test scraping the full poster a given game
full_poster = imdbScrape.scrape_full_poster(URL, DATA_LIMIT, "the last of us")
print("The link to the full poster of the last of us:")
print(full_poster)
print()

# test scraping all the posters of a dataset of 10 games
posters = imdbScrape.scrape_posters(URL, DATA_LIMIT)
print()

# test displaying all the games in a dataset of 10 games
imdbScrape.scrape_toString(URL, DATA_LIMIT)
