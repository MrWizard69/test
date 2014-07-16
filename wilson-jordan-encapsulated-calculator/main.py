import webapp2
from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()

        self.fifa = Games()
        self.fifa.title = "FIFA World Cup Brazil 2014"
        self.fifa.price = 39.88
        self.fifa.rating = "Rated E"
        self.fifa.genre = "Sports"
        self.fifa.synops = "An all-new feature and one of 100 new animations, Over-the-Back Headers give players the " \
                           "ability to jump over top of the opposition to win the ball."

        self.destiny = Games()
        self.destiny.title = "Destiny"
        self.destiny.price = 59.99
        self.destiny.rating = "Not Rated"
        self.destiny.genre = "Shooter"
        self.destiny.synops = "Destiny is an action game from the creators of Halo, set in a mysterious future."

        

class Games(object):
    def __init__(self):
        self.__title = ""
        self.__price = 0
        self.__rating = ""
        self.__genre = ""
        self.__synops = ""

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new):
        self.__title = new

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, money):
        self.__price = money

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, e):
        self.__rating = e

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, g):
        self.__genre = g

    @property
    def synops(self):
        return self.__synops

    @synops.setter
    def synops(self, s):
        self.__synops = s

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
