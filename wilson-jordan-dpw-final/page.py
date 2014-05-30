class MainHandler(webapp2.RequestHandler):
    def get(self):
        

class Page(object):
    def __init__(self):
        self.open = '''
        <!DOCTYPE html>
        <html>
        <head>
        <title></title>
        </head>
        <body> '''
        self._content = 'string'

        self._close = '''
        </body>
        </html>'''
