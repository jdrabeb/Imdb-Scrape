from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from videogame import Videogame

class imdbScrape:
    def scrape_games(pageUrl):
        games = []
        html = urlopen(pageUrl)
        bs = BeautifulSoup(html, 'html.parser')
        try:
            for element in bs.findAll("div", {"class": "lister-item mode-advanced"}):
                game = Videogame()
                game.set_link("www.imdb.com" + element.find("a")['href'])
                game.set_image(element.find("img")['src'])
                game.set_title(element.find("h3",
                    {"class": "lister-item-header"}).a.text)
                game.set_date(element.find("span",
                        {"class": re.compile("^lister-item-year.*")}).text)
                game.set_genre(element.find("span", {"class": "genre"}).text)
                game.set_rating(element.find("div",
                        {"class": re.compile(".ratings-imdb-rating")})['data-value'])
                game.set_description(element.findAll("p", {"text-muted"})[1].text)
                game.set_votes(element.find("span", {"name": "nv"})['data-value'])
                games.append(game)
        except AttributeError:
            print('Error')
        return games

