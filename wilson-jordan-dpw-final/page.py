class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        self.response.write(p.print_out())

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

class FormPage(Page):
    def __init__(self):
        Page.__init__(self)
        self.__form_open = '<form method="GET" action="">'
        self.__inputs = '''
        <input type="text" name="code" placeholder="placeholder" />
        <input type="submit" name="submit" />'''
        self.__form_close = '</form>'
        self.form_header = 'string'
        self.page_content = ''
        self._content = self.form_header + self.__form_open +self.__inputs + self.__form_close

