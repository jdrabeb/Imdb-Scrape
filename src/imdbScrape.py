from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv
from videogame import Videogame
from timed import timed

class imdbScrape:

    '''
    Scrape from the first number of given by data_limit the following data:
        -Title
        -Link
        -Image link
        -Release date
        -Genre
        -Rating
        -Description
        -Votes
    store them in a Videogame object and append it to list of games
    @return : list of games
    '''
    @timed(enabled=True)
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

    '''
    Display all video games scraped in a dataset limited by data_limit
    the display follows a predefined formatting
    '''
    @timed(enabled=True)
    def scrape_toString(pageUrl, data_limit):
        html = urlopen(pageUrl)
        bs = BeautifulSoup(html, 'html.parser')
        games = imdbScrape.scrape_games(pageUrl, data_limit)
        for game in games:
            print(game.toString())

    '''
    Scrape the full poster of a given video game title
    @return: the full poster
    '''
    @timed(enabled=True)
    def scrape_full_poster(pageUrl, data_limit, title):
        html = urlopen(pageUrl)
        bs = BeautifulSoup(html, 'html.parser')
        try:
            for element in bs.findAll("div",
                    {"class": "lister-item mode-advanced"})[:data_limit]:
                game_title = element.find("h3",
                    {"class": "lister-item-header"}).a.text
                if title.lower() in game_title.lower():
                    link = "http://www.imdb.com" + element.find("a")['href']
                    game_html = urlopen(link)
                    bs = BeautifulSoup(game_html, 'html.parser')
                    poster = "http://www.imdb.com" + bs.find(
                            "div", {"class": "poster"}).a['href']
        except AttributeError:
            print('Error')
        return poster

    '''
    Scrape a list of all the posters of a dataset of video games
    limited by data_limit
    @return: lists of miniature posters
    '''
    @timed(enabled=True)
    def scrape_posters(pageUrl, data_limit):
        posters = []
        html = urlopen(pageUrl)
        bs = BeautifulSoup(html, 'html.parser')
        try:
            for element in bs.findAll("div",
                    {"class": "lister-item mode-advanced"})[:data_limit]:
                poster = element.find("img")['loadlate']
                posters.append(poster)
        except AttributeError:
            print('Error')
        return posters

    '''
    Scrape the miniature poster of a given video game title
    @return: the miniature poster
    '''
    @timed(enabled=True)
    def scrape_poster_by_title(pageUrl, data_limit, title):
        html = urlopen(pageUrl)
        bs = BeautifulSoup(html, 'html.parser')
        try:
            for element in bs.findAll("div",
                    {"class": "lister-item mode-advanced"})[:data_limit]:
                game_title = element.find("h3",
                    {"class": "lister-item-header"}).a.text
                if title.lower() in game_title.lower():
                    poster = element.find("img")['loadlate']
                    return poster
        except AttributeError:
            print('Error')
            return None

