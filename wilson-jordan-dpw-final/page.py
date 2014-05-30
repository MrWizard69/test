class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        self.response.write(print_out())

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
        self.all = ''

    def print_out(self):
        self.update()
        return self.all

    def update(self):
        self.all = self.open + self._content + self._close
        self.all = self.all.format(**locals())

