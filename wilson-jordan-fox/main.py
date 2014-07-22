import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        cow = Cow()
        duck = Duck()
        fox = Fox()
        wildlife = [cow, duck, fox]
        self.response.write(p.print_out())

        if self.request.GET:
            animal = int(self.request.GET['wildlife'])

            name = wildlife[animal].name
            phylum = wildlife[animal].phylum
            w_class = wildlife[animal].w_class
            order = wildlife[animal].order
            family = wildlife[animal].family
            genus = wildlife[animal].genus
            url = wildlife[animal].url
            lifespan = wildlife[animal].lifespan
            habitat = wildlife[animal].habitat
            geo = wildlife[animal].geo
            sound = wildlife[animal].sound

            output = '''
            <div>
                <h1>{name}</h1>
                <div id="image">
                    <img src="{url}" alt="{name}" />
                </div>
                <div id="info">
                    <p>Phylum: {phylum}</p>
                    <p>Class: {w_class}</p>
                    <p>Order: {order}</p>
                    <p>Family: {family}</p>
                    <p>Genus: {genus}</p>
                    <p>Lifespan: {lifespan}</p>
                    <p>Habitat: {habitat}</p>
                    <p>Geolocation: {geo}</p>
                    <p>Sound: {sound}</p>
                </div>
            </div>'''

            result = output.format(**locals())
            self.response.write(result)


class Page(object):
    def __init__(self):
        self.header = '''
        <!DOCTYPE HTML>
        <html>
            <head>
                <title>{self.title}</title>
                <link rel="stylesheet" type="text/css" href="{self.css}" />
                <link href='{self.font}' rel='stylesheet' type='text/css'>
            </head>
            <body>'''
        self.content = '''
        <ul>
            <li><a href="?wildlife=0">Cow</a></li>
            <li><a href="?wildlife=1">Duck</a></li>
            <li><a href="?wildlife=2">Fox</a></li>
            <li><a href="http://localhost:13080/">Refresh</a></li>
        </ul>'''
        self.closer = '''
        </body>
        </html>'''

        self.__css = ''
        self.__title = ''
        self.__font = ''

    @property
    def css(self):
        return self.__title

    @css.setter
    def css(self, c):
            self.__css = c

    @property
    def title(self):
            return self.__title

    @title.setter
    def title(self,t):
            self.__title = t

    @property
    def font(self):
            return self.__font

    @font.setter
    def font(self,f):
            self.__font = f

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
        self.lifespan = '4 - 8 years'
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
