import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p1 = Page()
        p.form_header = "Enter your name:"
        p.css_url = "css/styles.css"
        self.response.write(p.print_out())


class Page(object):
    def __init__(self):
        self._open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>NYT App</title>
        <link rel="stylesheet" type="text/css" href="{self.css_url}" />
    </head>
    <body id="wrapper">'''
        self._content = 'This is my content'

        self._close = '''
    </body>
</html>'''
        self._css_url = ''
        self.all =''

    @property
    def css_url(self):
        return self._css_url

    @css_url.setter
    def css_url(self, c):
        self._css_url = c

    def print_out(self):
        self.update()
        return self.all

    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())


class FormPage(Page):
    def __init__(self):
        #call the constructor function of the parent
        Page.__init__(self)
        #super(FormPage, self).__init__()
        self.__form_open ='<form method="GET" action="">'
        self.__inputs ='''
    <select name="code">
        <option value="nyt">NYT News</option>
        <option value="iht">Herald Tribune</option>
        <option value="all">All</option>
    </select>

    <input type="submit" name="submit" />
    '''
        self.__form_close = '</form>'
        self.form_header = ">>Form Header<<"
        self.page_content = ''
        self._content = self.form_header + self.__form_open + self.__inputs + self.__form_close

    def update(self):
        self.all = self._open + self.form_header + self.__form_open + self.__inputs + self.__form_close + self.page_content + self._close
        #self.all = self.all.format(**locals())

