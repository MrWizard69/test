import webapp2
from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()

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
