import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        car1 = Car1()
        car1.color = 'Pink'
        car2 = Car2()
        car2.year = 2000
        car3 = Car3()
        car3.year = car1.year

        garage = [car1, car2, car3]

        self.response.write(p.print_out())

        if self.request.GET:
            car = int(self.request.GET['car'])
            name = garage[car].name
            year = garage[car].year
            color = garage[car].color

            results = '''
            <p>Name: {name}</p>
            <p>year: {year}</p>
            <p>color: {color}</p>
            '''
            update = results.format(**locals())
            self.response.write(update)


class Page(object):
    def __init__(self):
        self.header = '''
        <!DOCTYPE HTML>
        <html>
            <title>Inheritance Quiz</title>
        </html>
        <body>'''
        self.content = '''
            <ul>
                <li><a href="?car=0">Car1</a></li>
                <li><a href="?car=1">Car2</a></li>
                <li><a href="?car=2">Car3</a></li>
            </ul>
            '''
        self.closer = '''
        </body>
        </html>'''

    def print_out(self):
        page = self.header + self.content + self.closer
        update = page.format(**locals())
        return update

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
        self.year = 2014
        self.color = "Indigo"


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
