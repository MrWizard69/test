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


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
