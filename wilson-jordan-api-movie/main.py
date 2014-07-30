import webapp2
from xml.dom import minidom
import urllib2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()

        if self.request.GET:
            code = self.request.GET['code']
            m_model = MovieModel()
            m_model.code = self.request.GET['code']
            m_model.send_request()

            m_view = MovieView()
            m_view.movies = m_model.movies
            m_view.update()
            p.page_content = m_view.content

        self.response.write(p.print_out())

class Page(object):
    def __init__(self):
        self.header = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Movie App</title>
    </head>
    <body>
    <h1>Search For Your Favorite Movie</h1>
    '''
        self.content = 'Content'

        self.closer = '''
    </body>
<html>'''
        self.page = ''

    def print_out(self):
        self.update()
        return self.update

    def update(self):
        self.page = self.header + self.content + self.closer
        #self.update = self.page.format(**locals())

class FormPage(Page):
    def __init__(self):
        Page.__init__(self)
        super(FormPage, self).__init__()
        self.form_opener = '<form method="GET" action="">'
        self.inputs = '''
    <input type="text" name="code" placeholder="Movie Search" />
    <input type="submit" name="submit" />'''

        self.form_closer = '</form>'
        self.form_header = ''
        self.page_content = ''
        self.content = self.form_header + self.form_opener + self.inputs + self.form_closer

    def update(self):
        self.page = self.header + self.form_header + self.form_opener + self.inputs + self.form_closer + self.page_content + self.closer
        self.update = self.page.format(**locals())

class MovieObject(object):
    def __init__(self):
        self.title = ''
        self.rating = ''
        self.synops = ''
        self.open_date = ''
        self.image = ''
        self.movies = []

class MovieModel(object):
    def __init__(self):
        self.movies = []
        self.__mgo = ''
        self.__code = ''

    def send_request(self):
        url = 'http://api.nytimes.com/svc/movies/v2/reviews/search.xml?query='+ self.code +'&api-key=ea616c174e753fcadc69fccd2128aed5:19:69415137'
        req = urllib2.Request(url)
        opener = urllib2.build_opener()
        data = opener.open(req)
        xmldoc = minidom.parse(data)

        reviews = xmldoc.getElementsByTagName('review')

        for items in reviews:

            #print "test test test test"

            movies = MovieObject()
            #movies.title = items.getElementsByTagName('display_title')[0].firstChild.nodeValue
            #movies.rating = items.getElementsByTagName('mpaa_rating')[0].firstChild
            #movies.synops = items.getElementsByTagName('summary_short')[0].firstChild

            try:
                 movies.title = items.getElementsByTagName('display_title')[0].firstChild.nodeValue
            except:
                movies.title = 'No Title?'
                pass

            try:
                movies.rating = items.getElementsByTagName('mpaa_rating')[0].firstChild.nodeValue
            except:
                movies.rating = 'Not Rated'
                pass

            try:
                movies.synops = items.getElementsByTagName('summary_short')[0].firstChild.nodeValue
            except:
                movies.synops = 'No Information'
                pass

            try:
                movies.open_date = items.getElementsByTagName('opening_date')[0].firstChild.nodeValue
            except:
                movies.open_date = 'Not Released Yet'
                pass

            try:
                movies.image = items.getElementsByTagName('src')[0].firstChild.nodeValue
            except:
                movies.image = 'No Image'
            pass



            self.movies.append(movies)

    @property
    def mgo(self):
        return self.__mgo

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, c):
        self.__code = c

class MovieView(object):
    def __init__(self):
        self.mgo = MovieObject()
        self.content = ''
        self.movies = []

    def update(self):
        for review in self.movies:
            self.content +='''
            <div class="wrapper">
            <h1>'''+ review.title +'''</h1>
            <p>Rating: '''+ review.rating +'''</p>
            <p>Story: '''+ review.synops +'''</p>
            <p>Opening Date: '''+ review.open_date +'''</p>
            <img src="'''+ review.image +'''" />
            </div>
            '''


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
