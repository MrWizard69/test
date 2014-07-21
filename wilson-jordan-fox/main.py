import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        cow = Cow()
        duck = Duck()
        fox = Fox()
        wildlife = [cow, duck, fox]
        self.response.write(p.print_out())


class Page(object):
    def __init__(self):
        self.header = '''
        <!DOCTYPE HTML>
        <html>
            <head>
                <title></title>
            </head>
            <body>'''
        self.content = '''
        <ul>
            <li><a href="wildlife=0">Cow</a></li>
            <li><a href="wildlife=1">Duck</a></li>
            <li><a href="wildlife=2">Fox</a></li>
        </ul>'''
        self.closer = '''
        </body>
        </html>'''

    def print_out(self):
        return self.header + self.content + self.closer

class AbstractWildLife(object):
    def __init__(self):
        self.name = ''
        self.phylum = ''
        self.w_class = ''
        self.order = ''
        self.family = ''
        self.genus = ''
        self.url = ''
        self.lifespan = ''
        self.habitat = ''
        self.geo = ''
        self.sound = ''

class Cow(AbstractWildLife):
    def __init__(self):
        super(Cow,self).__init__()
        self.name = 'Cow'
        self.phylum = 'Chordata'
        self.order = 'Artiodactyla'
        self.w_class = 'Mammalia'
        self.family = 'Bovidae'
        self.genus = 'Bos Taurus'
        self.url = 'images/cow.jpg' #wiki commons
        self.lifespan = '15 years'
        self.habitat = 'Grasslands and Forests'
        self.geo = 'On farms everywhere'
        self.sound = 'MEROOOOO'

class Duck(AbstractWildLife):
    def __init__(self):
        super(Duck,self).__init__()
        self.name = 'Duck'
        self.phylum = 'Chordata'
        self.order = 'Anseriformes'
        self.w_class = 'Aves'
        self.family = 'Anatide'
        self.genus = 'Duck'
        self.url = 'images/duck.jpg' #wiki commons
        self.lifespan = ' 4 - 8 years'
        self.habitat = 'Rivers, lakes and woodland wetlands'
        self.geo = 'At a pond near you'
        self.sound = 'QUACK QUACK QUACK'

class Fox(AbstractWildLife):
    def __init__(self):
        super(Fox,self).__init__()
        self.name = 'Fox'
        self.phylum = 'Chordata'
        self.w_class = 'Mammalia'
        self.order = 'Carnivora'
        self.family = 'Canidae'
        self.genus = 'Canis'
        self.url = 'images/fox.jpg' #wiki commons
        self.lifespan = '5 years'
        self.habitat = 'The northern hemisphere from the Arctic Circle to North Africa, and Central America.'
        self.geo = 'Everywhere'
        self.sound = 'Ring-ding-ding-ding-dingeringeding!'



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
