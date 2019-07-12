from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.hybrid import hybrid_property
from app import create_app

db, app = create_app()

class Videogame(db.Model):
    __tablename__ = 'games'

    game_id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    link = Column(String(150), nullable=False)
    image = Column(String(150), nullable=False)
    genre = Column(String(80), nullable=False)
    date = Column(String(80), nullable=False)
    rating = Column(String(80), nullable=False)
    description = Column(String(80), nullable=False)
    votes = Column(String(80), nullable=False)

    def __init__(
            self, game_id = None, title = None, link = None, image = None, genre = None,
            date = None, rating = None, description = None, votes = None):
        self.game_id = game_id
        self.title = title
        self.link = link
        self.image = image
        self.genre = genre
        self.date = date
        self.rating = rating
        self.description = description
        self.votes = votes

    def __repr__(self):
        return "<Game(title='%s', genre='%s', date='%s')>" % (
                                self.title, self.genre, self.date)


    def set_title(self, title):
        self.title = title

    def set_link(self, link):
        self.link = link

    def set_image(self, image):
        self.image = image

    def set_genre(self, genre):
        self.genre = genre

    def set_date(self, date):
        self.date = date

    def set_rating(self, rating):
        self.rating = rating

    def set_description(self, description):
        self.description = description

    def set_votes(self, votes):
        self.votes = votes

    def get_title(self):
        return self.title

    def get_link(self):
        return self.link

    def get_image(self):
        return self.image

    def get_genre(self):
        return self.genre

    def get_date(self):
        return self.date

    def get_rating(self):
        return self.rating

    def get_description(self):
        return self.description

    def get_votes(self):
        return self.votes

    def toString(self):
        print("title: " + self.title +
                ", genre: " + self.genre +
                ", release date: " + self.date +
                ", rating: " + self.rating +
                ", description: " + self.description +
                ", votes: " + self.votes)

db.session.remove()
db.drop_all()
db.create_all()
