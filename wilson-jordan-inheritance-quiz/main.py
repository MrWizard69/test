import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class Page(object):
    def __init__(self):
        self.header = '''
        <!DOCTYPE HTML>
        <html>
            <title></title>
        </html>
        <body>'''
        self.content = '''
            Content
            '''
        self.closer = '''
        </body>
        </html>'''

    def print_out(self):
        return self.header + self.content + self.closer

class AbCar(object):
    def __init__(self):
        self.name = ''
        self.__year = 0
        self.color = ''
    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y):
        self.__year = y

class Car1(AbCar):
    def __init__(self):
        super(Car1, self).__init__()
        self.name = "Shelby"
        self.year = 1969
        self.color = "Red"

class Car2(AbCar):
    def __init__(self):
        super(Car2, self).__init__()
        self.name = "Thomas"
        self.year = 2003
        self.color = "Yellow"

class Car3(AbCar):
    def __init__(self):
        super(Car3, self).__init__()
        self.name = "Missy"
        self.year = "2014"
        self.color = "Indigo"


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
