from videogame import Videogame
from imdbScrape import imdbScrape

URL = 'https://www.imdb.com/search/title/?genres=drama&sort=user_rating&title_type=game'
DATA_LIMIT = 10

poster = imdbScrape.scrape_poster_by_title(URL, DATA_LIMIT, "The last of us")
print("The link to the poster of the last of us:")
print(poster)
print()
full_poster = imdbScrape.scrape_full_poster(URL, DATA_LIMIT, "the last of us")
print("The link to the full poster of the last of us:")
print(full_poster)
print()
posters = imdbScrape.scrape_posters(URL, DATA_LIMIT)
print()
imdbScrape.scrape_toString(URL, DATA_LIMIT)
