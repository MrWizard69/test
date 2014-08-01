import webapp2
from xml.dom import minidom
import urllib2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.title = "Final"
        p.h1 = "God help us all..."

        code = self.request.GET['code']


        if self.request.GET:
            g_model = ThronesModel()
            g_model.houses = code
            g_model.send_request()

            g_view = ThronesView()
            g_view.house = g_model.house
            g_view.update()
            p.content = g_view.content

        self.response.write(p.print_out())

class Page(object):
    def __init__(self):
        self.header = '''
<DOCTYPE HTML>
<html>
<head>
    <title>{self.title}</title>
</head>
<body>
'''
        self.content = '''
        <h1>{self.h1}</h1>
        <a href="?code=0">Link1</a>
        <a href="?code=1">Link2</a>
        <a href="?code=2">Link3</a>
        <a href="?code=3">Link4</a>
        <a href="?code=4">Link5</a>
        <a href="?code=5">Link6</a>
        '''

        self.closer = '''
</body>
</html>'''
        self.page = ''
        self._title = ''
        self.__h1 = ''

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, t):
        self._title = t

    @property
    def h1(self):
        return self.__h1

    @h1.setter
    def h1(self, h):
        self.__h1 = h

    def print_out(self):
        self.update()
        return self.update

    def update(self):
        self.page = self.header + self.content + self.closer
        self.update = self.page.format(**locals())



class ThronesObject(object):
    def __init__(self):
        self.name = ''
        self.sigil = ''
        self.motto = ''
        self.color1 = ''
        self.color2 = ''
        self.head = ''
        self.image = ''
        self.house = []

class ThronesModel(object):
    def __init__(self):
        self.house = []
        self.tgo = ''
        self.code = 'got.xml'

    def send_request(self):
        url = 'http://rebeccacarroll.com/api/got/' + self.code
        req = urllib2.Request(url)
        opener = urllib2.build_opener()
        data = opener.open(req)
        xmldoc = minidom.parse(data)

        thrones = xmldoc.getElementsByTagName('house')

        #print 'test test test test!!!!!!!!!!'


        for item in thrones:
            throne = ThronesObject()

            try:
                throne.name = item.getElementsByTagName('name')[0].firstChild.nodeValue
            except:
                throne.name = 'No Name'

            try:
                throne.sigil = item.getElementsByTagName('sigil')[0].firstChild.nodeValue
            except:
                throne.sigil = 'No Sigil'

            try:
                throne.motto = item.getElementsByTagName('motto')[0].firstChild.nodeValue
            except:
                throne.motto = 'No Motto'

            try:
                throne.color1 = item.getElementsByTagName('color1')[0].firstChild.nodeValue
            except:
                throne.color1 = 'No Color'

            try:
                throne.color2 = item.getElementsByTagName('color2')[0].firstChild.nodeValue
            except:
                throne.color2 = 'No Color'

            try:
                throne.head = item.getElementsByTagName('head')[0].firstChild.nodeValue
            except:
                throne.head = 'No Head'

            try:
                throne.image = item.getElementsByTagName('image')[0].firstChild.nodeValue
            except:
                throne.image = ''

            self.house.append(throne)



class ThronesView(object):
    def __init__(self):
        self.tgo = ThronesObject()
        self.content = ''
        self.house = []




    def update(self):
        for thrones in self.house:
            self.content += '''
            <h1>Name: ''' + thrones.name + '''</h1>
            <p>Sigil: ''' + thrones.sigil + '''</p>
            <p>Motto: ''' + thrones.motto + '''</p>
            <p>Color1: ''' + thrones.color1 + '''</p>
            <p>Color2: ''' + thrones.color2 + '''</p>
            <p>Head: ''' + thrones.head + '''</p>
            <img src="''' + thrones.image + '''" />
            '''


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
