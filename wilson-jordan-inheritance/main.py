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
        

        self.response.write(p)

class Page(object):
    def __init__(self):

        self.avr = ""
        self.gpa = ""
        self.grd = ""

class school(Page):
    def __init__(self):
        Page.__init__(self)

    def join(self, filler):
        self.avr = filler.avr
        self.gpa = filler.gpa
        self.grd = filler.grd

class Grade(school):
        def __init__(self):
            school.__init__(self)
            pl = school()
            pl.avr = "86"
            pl.gpa = "3.33"
            pl.grd = "B+"

            self.join(Grade)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
