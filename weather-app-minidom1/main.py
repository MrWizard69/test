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
import urllib2
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #setting up the basic page
        view = FormPage()
        view.form_header = "Open Weather Map API"


        #if there are url variables...
        if self.request.GET:
            code = self.request.GET['code']
            url = 'http://api.openweathermap.org/data/2.5/weather?q=' + code
            #go get the api info
            req = urllib2.Request(url)
            opener = urllib2.build_opener()
            data = opener.open(req)

            #parse it
            jsondoc = json.load(data)
            content = jsondoc['main']['temp']
            view.page_content = "Temperature in Kelven: " + str(content) + '&deg;'
            view.page_content += "<br/>Temperature in Farenheit: " + str(1.8*(content-273) + 32) + '&deg;'

        #print out
        self.response.write(view.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
