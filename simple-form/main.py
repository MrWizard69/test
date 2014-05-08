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
import webapp2
#from FILE import CLASSNAME
from page import HTMLPage

#blueprint for creating our web app
class MainHandler(webapp2.RequestHandler):
    #catalyst - gets our web app going
    #when this app loads.. this function gets called automagically
    def get(self):
        #prints out to the web browser
        #self.response.write('Hello world!')
        p = HTMLPage()#calls constructor __init__ function inside HTMLPage class
        ##atributes:
            #   instance.attribute
        ##methods:
            #   instance.method()
        if self.request.GET:
            fn = self.request.GET['firstname']
            ln = self.request.GET['lastname']
            self.response.write(p.print_out(fn +' ' + ln))
        else:
            self.response.write(p.print_out(" "))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
