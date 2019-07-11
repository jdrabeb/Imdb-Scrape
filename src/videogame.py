class Videogame:
    def __init__(
            self, title = None, link = None, image = None, genre = None,
            date = None, rating = None, description = None, votes = None):
        self.title = title
        self.link = link
        self.image = image
        self.genre = genre
        self.date = date
        self.rating = rating
        self.description = description
        self.votes = votes

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

    def toString(self):
        print("title: " + self.title +
                ", genre: " + self.genre +
                ", release date: " + self.date +
                ", rating: " + self.rating +
                ", description: " + self.description +
                ", votes: " + self.votes)

