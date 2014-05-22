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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        self.response.write('Hello world!')

class Page(object):
    def __init__(self):
        self.__open ='''
        <!DOCTYPE HTML>
        <html>
        <head>
            <title>Count it up</title>
        </head>
        <body>

            <a href="cnt=counter">Count Up</a>'''

        self.__close = '''
        </body>
        </html>'''

        self.__html = self.__open + self.__close

    @property
    def counter(self):
        return self.__counter

    @counter.setter
    def counter(self, new_cnt):
        self.__counter = new_cnt
        self.update()

    def print_out(self):
        return self.__html

    def update(self):
        self.__html = self.__html.format(**locals())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
