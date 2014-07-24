import jinja2
import os
import urllib
import webapp2

from apiclient.discovery import build

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

API_KEY = "AIzaSyDOkg-u9jnhP-WnzX5WPJyV1sc5QQrtuyc"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
QUERY_TERM = "four owls"

class MainHandler(webapp2.RequestHandler):
  def get(self):
    self.search_by_keyword()

  def search_by_keyword(self):
    youtube = build(
      YOUTUBE_API_SERVICE_NAME, 
      YOUTUBE_API_VERSION, 
      developerKey=API_KEY
    )
    search_response = youtube.search().list(
      q=QUERY_TERM,
      part="id,snippet",
      maxResults=5
    ).execute()
    
    videos = []

    for search_result in search_response.get("items", []):
      videos.append(search_result)

    template_values = {
      'videos': videos
    }

    self.response.headers['Content-type'] = 'text/html'
    template = JINJA_ENVIRONMENT.get_template('index.html')
    self.response.write(template.render(template_values))
        
app = webapp2.WSGIApplication([
  ('/.*', MainHandler),
], debug=True)
