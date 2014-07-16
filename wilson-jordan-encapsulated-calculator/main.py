import webapp2
from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        #self.response.write(p.print_out())

        self.fifa = Games()
        self.fifa.title = "FIFA World Cup Brazil 2014"
        self.fifa.price = 39.88
        self.fifa.rating = "Rated E"
        self.fifa.genre = "Sports"
        self.fifa.synops = "An all-new feature and one of 100 new animations, Over-the-Back Headers give players the " \
                           "ability to jump over top of the opposition to win the ball."
        self.fifa.calc_all_games_pi()

        self.destiny = Games()
        self.destiny.title = "Destiny"
        self.destiny.price = 59.99
        self.destiny.rating = "Not Rated"
        self.destiny.genre = "Shooter"
        self.destiny.synops = "Destiny is an action game from the creators of Halo, set in a mysterious future."
        self.destiny.calc_all_games_pi()

        self.titan = Games()
        self.titan.title = "Titanfall"
        self.titan.price = 49.80
        self.titan.rating = "Not Rated"
        self.titan.genre = "Shooter"
        self.titan.synops = "Crafted by one of the co-creators of Call of Duty and other key developers behind the " \
                            "Call of Duty franchise."
        self.titan.calc_all_games_pi()

        self.minecraft = Games()
        self.minecraft.title = "Minecraft"
        self.minecraft.price = 19.96
        self.minecraft.rating = "Rated E"
        self.minecraft.genre = "Adventure"
        self.minecraft.synops = "Minecraft is a game about breaking and placing blocks."
        self.minecraft.calc_all_games_pi()

        self.grand = Games()
        self.grand.title = "Grand Theft Auto V"
        self.grand.price = 32.99
        self.grand.rating = "Rated M"
        self.grand.genre = " Action / Adventure "
        self.grand.synops = "Grand Theft Auto V takes place in a re-imagined, present-day Southern California in the " \
                            "largest and most thriving game-world."
        self.grand.calc_all_games_pi()

        games = [self.fifa, self.destiny, self.titan, self.minecraft, self.grand]

        if self.request.GET:
            game = int(self.request.GET['game'])

            title = games[game].title
            price = games[game].price
            rating = games[game].rating
            genre = games[game].genre
            synops = games[game].synops
            pi_games = games[game].pi_games

            game_info = '''
                <div>
                    <p>{title}</p>
                    <p>{price}</p>
                    <p>{rating}</p>
                    <p>{genre}</p>
                    <p>{synops}</p>
                    <p>{pi_games}</p>
                </div>
            '''

            all_games = game_info.format(**locals())

            self.response.write(all_games)

        self.response.write(p.print_out())



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

    @property
    def pi_games(self):
        return self.__pi_games

    def calc_all_games_pi(self):
        total = self.__price / 3.14
        self.__pi_games = total




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
