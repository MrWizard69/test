import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


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
            <li></li>
            <li></li>
            <li></li>
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
        self.phylum = 'Mammalia'
        self.order = 'Artiodactyla'
        self.family = 'Bovidae'
        self.genus = 'Bos Taurus'
        self.url = 'http://upload.wikimedia.org/wikipedia/commons/0/0c/Cow_female_black_white.jpg' #wiki commons
        self.lifespan = '15 years'
        self.habitat = 'Grasslands and Forests'
        self.geo = 'On farms everywhere'
        self.sound = 'MEROOOOO'

class Duck(AbstractWildLife):
    def __init__(self):
        super(Duck,self).__init__()
        self.name = 'Duck'



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
