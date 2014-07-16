import webapp2
from views import Page #you can use * to access all the classes from views

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        #send in content we want
        p.content = "Sign the form below:"
        p.css = "css/styles.css"
        #p.title = "Welcome"
        #print out the content to the browser
        self.response.write(p.print_out())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
