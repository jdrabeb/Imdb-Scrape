from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv
from videogame import Videogame

class imdbScrape:
    def scrape_games(pageUrl, data_limit):
        games = []
        html = urlopen(pageUrl)
        bs = BeautifulSoup(html, 'html.parser')
        try:
            for element in bs.findAll("div",
                    {"class": "lister-item mode-advanced"})[:data_limit]:
                game = Videogame()
                game.set_link("http://www.imdb.com" + element.find("a")['href'])
                game.set_image(element.find("img")['loadlate'])
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

    def create_csv(games):
        with open('games.csv', mode='w') as csv_file:
            fieldnames = ['title', 'link', 'image', 'date', 'genre', 'rating',
                   'description', 'votes']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for game in games:
                writer.writerow({'title': game.get_title()})
                writer.writerow({'link': game.get_link()})
                writer.writerow({'image': game.get_image()})
                writer.writerow({'date': game.get_date()})
                writer.writerow({'genre': game.get_genre()})
                writer.writerow({'rating': game.get_rating()})
                writer.writerow({'description': game.get_description()})
                writer.writerow({'votes': game.get_votes()})

