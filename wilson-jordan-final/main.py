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

class ThronesObject(object)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
