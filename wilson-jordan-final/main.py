import webapp2
from xml.dom import minidom
import urllib2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()

        self.response.write(p.print_out())

class Page(object):
    def __init__(self):
        self. header = '''
<DOCTYPE HTML>
<html>
<head>
    <title></title>
</head>
<body>
'''
        self.content = 'content'

        self.closer = '''
</body>
</html>'''
        self.page = ''

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

    def send_request(self):
        url = 'http://rebeccacarroll.com/api/got/got.xml'
        req = urllib2.Request(url)
        opener = urllib2.build_opener()
        data = opener.open(req)
        xmldoc = minidom.parse(data)

        throne = xmldoc.getElementsByTagName('houses')

        for item in throne:
            house = ThronesObject()

            try:
                house.name = item.getElementsByTagName('name')[0].firstChild.nodeValue
            except:
                house.name = 'No Name'


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
