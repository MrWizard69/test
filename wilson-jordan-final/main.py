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

            try:
                house.sigil = item.getElementsByTagName('sigil')[0].firstChild.nodeValue
            except:
                house.sigil = 'No Sigil'

            try:
                house.motto = item.getElementsByTagName('motto')[0].firstChild.nodeValue
            except:
                house.motto = 'No Motto'

            try:
                house.color1 = item.getElementsByTagName('color1')[0].firstChild.nodeValue
            except:
                house.color1 = 'No Color'

            try:
                house.color2 = item.getElementsByTagName('color2')[0].firstChild.nodeValue
            except:
                house.color2 = 'No Color'

            try:
                house.head = item.getElementsByTagName('head')[0].firstChild.nodeValue
            except:
                house.head = 'No Head'

            try:
                house.image = item.getElementsByTagName('image')[0].firstChild.nodeValue
            except:
                house.image = ''

        self.house.append(throne)

class ThronesView(object):
    def __init__(self):
        self.tgo = ThronesObject()
        self.content = ''
        self.house = []

    def update(self):
        for thrones in self.house:
            self.content += '''
            <h1>''' + thrones.name + '''</h1>
            <p>''' + thrones.sigil + '''</p>
            <p>''' + thrones.motto + '''</p>
            <p>''' + thrones.color1 + '''</p>
            <p>''' + thrones.color2 + '''</p>
            <p>''' + thrones.color1 + '''</p>
            <p>''' + thrones.head + '''</p>
            <img src="''' + thrones.image + '''" />
            '''


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
