#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#Jordan Wilson
#Class
#date
import webapp2
from page import FormPage
from xml.dom import minidom #library for working with xml in python
import urllib2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #setting up the basic page
        view = FormPage()
        view.form_header = "Yahoo Weather App"


        #if there are url variables...
        if self.request.GET:
            code = self.request.GET['code']
            url = 'http://xml.weather.yahoo.com/forecastrss?p=' + code
            #go get the api info
            req = urllib2.Request(url)
            opener = urllib2.build_opener()
            data = opener.open(req)

            #parse it
            xmldoc = minidom.parse(data)

            #look at elements within the xml
            #self.response.write(xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue)
            list = xmldoc.getElementsByTagName('yweather:forecast')
            content = xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue + "<br/>"
            for item in list:
                content += item.attributes['day'].value
                content +=" | High of: " + item.attributes['high'].value
                content +=" | Low of: " + item.attributes['low'].value
                content +=" | Condition: " + item.attributes['text'].value
                content +='<img width ="60" src="images/' + item.attributes['code'].value + '.png"/>'
                content += '<br/>'
            #self.response.write(content)
            view.page_content = content #passing that string into our instance form

        #print out
        self.response.write(view.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
