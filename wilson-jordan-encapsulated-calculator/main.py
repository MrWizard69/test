import webapp2
from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        self.response.write(p.print_out()) #display the page

        self.fifa = Games() #fifa game
        self.fifa.title = "FIFA World Cup Brazil 2014"
        self.fifa.price = 39.88
        self.fifa.rating = "E"
        self.fifa.genre = "Sports"
        self.fifa.synops = "An all-new feature and one of 100 new animations, Over-the-Back Headers give players the " \
                           "ability to jump over top of the opposition to win the ball."
        self.fifa.calc_all_games_pi() #calculates the price / pi

        self.destiny = Games() #destiny game
        self.destiny.title = "Destiny"
        self.destiny.price = 59.99
        self.destiny.rating = "Not Rated"
        self.destiny.genre = "Shooter"
        self.destiny.synops = "Destiny is an action game from the creators of Halo, set in a mysterious future."
        self.destiny.calc_all_games_pi() #calculates the price / pi

        self.titan = Games() #titanfall game
        self.titan.title = "Titanfall"
        self.titan.price = 49.81
        self.titan.rating = "Not Rated"
        self.titan.genre = "Shooter"
        self.titan.synops = "Crafted by one of the co-creators of Call of Duty and other key developers behind the " \
                            "Call of Duty franchise."
        self.titan.calc_all_games_pi() #calculates the price / pi

        self.minecraft = Games() #minecraft game
        self.minecraft.title = "Minecraft"
        self.minecraft.price = 19.96
        self.minecraft.rating = "E"
        self.minecraft.genre = "Adventure"
        self.minecraft.synops = "Minecraft is a game about breaking and placing blocks."
        self.minecraft.calc_all_games_pi() #calculates the price / pi

        self.grand = Games() #grand theft auto game
        self.grand.title = "Grand Theft Auto V"
        self.grand.price = 32.99
        self.grand.rating = "M"
        self.grand.genre = " Action / Adventure "
        self.grand.synops = "Grand Theft Auto V takes place in a re-imagined, present-day Southern California in the " \
                            "largest and most thriving game-world."
        self.grand.calc_all_games_pi() #calculates the price / pi

        games = [self.fifa, self.destiny, self.titan, self.minecraft, self.grand] #an array to hold all the info

        if self.request.GET:
            game = int(self.request.GET['game'])

            #making variables to hold specific values of each game
            title = games[game].title
            price = games[game].price
            rating = games[game].rating
            genre = games[game].genre
            synops = games[game].synops
            pi_games = games[game].pi_games

            #below is where all the variables are being displayed
            game_info = '''
                <div class="form">
                    <p>Title: {title}</p>
                    <p>Price: {price}</p>
                    <p>Rating: {rating}</p>
                    <p>Genre: {genre}</p>
                    <p>Synopsis: {synops}</p>
                    <p>The price / pi: {pi_games}...</p>
                </div>
            '''

            all_games = game_info.format(**locals())


            self.response.write(all_games) #display the game information

        #self.response.write(p.print_out())



class Games(object): #this is my constructor
    def __init__(self):
        self.__title = ""
        self.__price = 0
        self.__rating = ""
        self.__genre = ""
        self.__synops = ""

    #below is a bunch of getters and setters
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

    def calc_all_games_pi(self): #this is where the price is calced with pi
        total = self.__price / 3.14
        self.__pi_games = total




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
