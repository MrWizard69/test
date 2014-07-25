import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class Page(object):
    def __init__(self):
        self.opener = '''
        <DOCTYPE HTML>
        <head>
            <title></title>
        </head>
        <body>'''
        self.content = '''
        content
        '''
        self.closer = '''
        </body>
        </html>'''

        self.page = self.opener + self.content + self.closer

    def print_out(self):
        self.update = self.page.format(**locals())
        return self.update


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
