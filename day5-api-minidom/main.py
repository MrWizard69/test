import webapp2
import urllib2
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #p = Page()
        f = FormPage()
        f.inputs = [{'type':'text', 'placeholder':'Zip Code', 'name':'zip'},
                {'type':'submit', 'value':'Get Weather', 'name':'submit'}]
        #puts our inputs in the content var
        #if there is key value pairs in the URL request... do stuff
        if self.request.GET:
            zip = self.request.GET['zip']
            # load in info from the api
            #load info from api****
            #build request - format the official request
            request = urllib2.Request("http://xml.weather.yahoo.com/forecastrss?p=" + zip)

            #create an object that fetches responses/pages from server
            opener = urllib2.build_opener()

            #tell object to go fetch response
            data = opener.open(request)

            #parse the info
            xmldoc = minidom.parse(data)
            titles = xmldoc.getElementById("title")
            print titles
        else:
            self.response.write(f.print_out())



class Page(object):
    _head = '''<!DOCTYPE HTML>
<head>
    <title>Inheritance Demo</title>
</head>
<body>'''
    _content = ''

    _close = '''
</body>
</html>'''

    def __init__(self):
        pass

    def print_out(self):
        return self._head + self._content + self._close

class FormPage(Page):
    __inputs = []
    _form_open = "<form method=\"GET\" action="" />"
    _form_close = "</form>"

    def __init__(self):
        #invoke constructor in parent/superclass
        Page.__init__(self)

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, i):
        self.__inputs = i

    def create_inputs(self):
        #accept an array of dictionaries
        #use it to build out form <input> elements
        tot_inputs = ''
        for i in self.__inputs:
            #for each item in our __inputs array
            tot_inputs += '<input type="' + i['type'] + '" name="' + i['name'] +'"'
            if 'placeholder' in i:
                tot_inputs += ' placeholder="' + i['placeholder'] + '"'
            if 'value' in i:
                tot_inputs += ' value="' + i['value'] + '"'
            tot_inputs += ' />'
        return tot_inputs
        #Page.print_out() This will print out the page class and not the form class

    #*** this function overrides the printout function in the page class ***
    def print_out(self):
        return self._head + self._form_open + self.create_inputs() + self._form_close + self._close

'''
    def print_out(self):
        self._head + self._form_open + self.create_inputs() + self._form_close + self._close
         return Page.print_out(self)

'''




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
