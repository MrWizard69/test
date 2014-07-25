import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        c = Counter()
        p.counter = 0

        if self.request.GET:
            c.counter += 1
            self.response.write(c.counter)

        self.response.write(p.print_out())





class Page(object):
    def __init__(self):
        self.opener = '''
        <DOCTYPE HTML>
        <head>
            <title></title>
        </head>
        <body>'''
        self.content = '''
        <a href="?counter=0">Count Up</a>
        '''
        self.closer = '''
        </body>
        </html>'''

        self.page = self.opener + self.content + self.closer

    def print_out(self):
        self.update = self.page.format(**locals())
        return self.update

class Counter(object):
    def __init__(self):
        self.__counter = 0

    @property
    def counter(self):
        return self.__counter

    @counter.setter
    def counter(self, c):
        self.__counter = c



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
