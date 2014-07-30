import webapp2
from xml.dom import minidom # this makes xml work in python
import urllib2
from urllib import quote # this makes it possible to type more than one word into the text box


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage() # this references the form page class

        if self.request.GET:
            code = self.request.GET['code']
            m_model = MovieModel() # creates an instance of the model
            m_model.code = self.request.GET['code'] # passes the var to the model
            m_model.send_request() # connects to the API

            m_view = MovieView() # the view that's going to show the info
            m_view.movies = m_model.movies
            m_view.update() # creates the html
            p.page_content = m_view.content

        self.response.write(p.print_out())

class Page(object): # this is the basic page of the app
    def __init__(self):
        self.header = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Movie App</title>
        <link rel="stylesheet" type="text/css" href="css/styles.css" />
        <link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Droid+Sans" />
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

class FormPage(Page): # this is the form. The form page will actually make the page class around it so all the contents are together
    def __init__(self):
        Page.__init__(self)
        super(FormPage, self).__init__()
        self.form_opener = '<form method="GET" action="">'
        self.inputs = '''
    <input id="search" type="text" name="code" autofocus placeholder="Movie Search" />
    <input id="submit" type="submit" name="submit" value="Search" />'''

        self.form_closer = '</form>'
        self.form_header = ''
        self.page_content = ''
        self.content = self.form_header + self.form_opener + self.inputs + self.form_closer

    def update(self):
        self.page = self.header + self.form_header + self.form_opener + self.inputs + self.form_closer + self.page_content + self.closer
        self.update = self.page.format(**locals())

class MovieObject(object): # all the info I want to get from the xml
    def __init__(self):
        self.title = ''
        self.rating = ''
        self.synops = ''
        self.open_date = ''
        self.image = ''
        self.movies = []

class MovieModel(object): # this is where the information is passed from the text box and to the api.
    def __init__(self):
        self.movies = []
        self.__mgo = ''
        self.__code = 'movie'

    def send_request(self):
        safe_code = quote(self.code, safe="%/:=&?~#+!$,;'@()*[]") # this line allows users to type for example "The Matrix" instead of just "Matrix"
        url = 'http://api.nytimes.com/svc/movies/v2/reviews/search.xml?query='+ safe_code +'&api-key=ea616c174e753fcadc69fccd2128aed5:19:69415137' # this passes what what ever the user typed in to the url
        req = urllib2.Request(url)
        opener = urllib2.build_opener()
        data = opener.open(req)
        xmldoc = minidom.parse(data)

        reviews = xmldoc.getElementsByTagName('review')

        for items in reviews: # this loop will go through each movie and look to see if each element of information exists, if not place holder info

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
                movies.image = 'images/idk.jpg'
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

class MovieView(object): # this is where the info is actually displayed. Each movie is put into its own container.
    def __init__(self):
        self.mgo = MovieObject()
        self.content = ''
        self.movies = []

    def update(self):
        for review in self.movies:
            self.content +='''
            <div class="wrapper">
            <h2>'''+ review.title +'''</h2>
            <p>Rating: '''+ review.rating +'''</p>
            <p>Story: '''+ review.synops +'''</p>
            <img width="100px" height="100px" src="'''+ review.image +'''" />
            <p>Opening Date: '''+ review.open_date +'''</p>
            </div>
            '''


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
