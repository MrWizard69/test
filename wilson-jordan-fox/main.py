import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page() # a reference to the page class

        p.title = 'What Does The Fox Say??' # my title
        p.font = 'http://fonts.googleapis.com/css?family=Droid+Sans' # the font I used
        p.css = 'css/styles.css' # where my style sheet is
        cow = Cow() # a reference to the cow subclass
        duck = Duck() # a reference to the duck subclass
        fox = Fox() # a reference to the fox subclass
        wildlife = [cow, duck, fox] # my array of animals
        self.response.write(p.print_out())

        if self.request.GET:
            animal = int(self.request.GET['wildlife'])
            #this is where the values are applied
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
            # this is where it is displayed
            output = '''
            <div>
                <h1>{name}</h1>
                <div id="info">
                    <img src="{url}" alt="{name}" />
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

# this is the where all the content resides
class Page(object):
    def __init__(self):
        self.header = '''
        <!DOCTYPE HTML>
        <html>
            <head>
                <title>{self.title}</title>
                <link rel="stylesheet" type="text/css" href="{self.css}" />
                <link href="{self.font}" rel='stylesheet' type='text/css'>
            </head>
            <body>'''
        self.content = '''
        <ul>
            <li><a href="?wildlife=0">Cow</a></li>
            <li><a href="?wildlife=1">Duck</a></li>
            <li><a href="?wildlife=2">Fox</a></li>
            <li><a href="http://localhost:13080/">Refresh</a></li>
        </ul>
        <div id="info">
            <p>Cow goes moo and ducks go quack quack. But there's one sound that no one knows... WHAT DOES THE FOX SAY?</p>
        </div>
        '''
        self.closer = '''
        </body>
        </html>'''

        self.__css = ''
        self.__title = ''
        self.__font = ''
    # a getter
    @property
    def css(self):
        return self.__css
    # and a setter
    @css.setter
    def css(self, c):
            self.__css = c
    # a getter
    @property
    def title(self):
            return self.__title
    # and a setter
    @title.setter
    def title(self, t):
            self.__title = t
    # a getter
    @property
    def font(self):
            return self.__font
    # and a setter
    @font.setter
    def font(self, f):
            self.__font = f


    #when everything is said and done this is where all the information ais spat out
    def print_out(self):
        page = self.header + self.content + self.closer
        output = page.format(**locals())
        return output
#the basic constructor where all the value place holders are made
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

#my cow subclass
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
#my duck subclass
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
#my fox subclass
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
        self.habitat = 'Just about everywhere'
        self.geo = 'Everywhere'
        self.sound = 'Ring-ding-ding-ding-dingeringeding!'



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
