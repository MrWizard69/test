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
        lemons = 1
        sugar = 3
        cups = 2
        pitcher = 10

        suzie = lemstand()
        suzie.lem = 10 * lemons
        suzie.sug = 3 * sugar
        suzie.cup = 2 * cups
        suzie.pit = 1 * pitcher
        suzie.total = suzie.lem + suzie.sug + suzie.cup + suzie.pit
        suzie.update()
        self.response.write("Suzie needs "+ suzie.print_info() + " for supplies")

        brian = lemstand()
        brian.lem = 33 * lemons
        brian.sug = 6 * sugar
        brian.cup = 5 * cups
        brian.pit = 2 * pitcher
        brian.total1 = brian.lem + brian.sug + brian.cup + brian.pit
        brian.update()
        self.response.write(brian.print_info())

        cindy = lemstand()
        cindy.lem = 66 * lemons
        cindy.sug = 10 * sugar
        cindy.cup = 25 * cups
        cindy.pit = 4 * pitcher
        cindy.total2 = cindy.lem + cindy.sug + cindy.cup + cindy.pit
        cindy.update()
        self.response.write(cindy.print_info())

        david = lemstand()
        david.lem = 66 * lemons
        david.sug = 10 * sugar
        david.cup = 25 * cups
        david.pit = 4 * pitcher
        david.total3 = david.lem + david.sug + david.cup + david.pit
        david.update()
        self.response.write(david.print_info())

        adri = lemstand()
        adri.lem = 100 * lemons
        adri.sug = 50 * sugar
        adri.cup = 100 * cups
        adri.pit = 10 * pitcher
        adri.total4 = adri.lem + adri.sug + adri.cup + adri.pit
        adri.update()
        self.response.write(adri.print_info())


class lemstand(object):
    def __init__(self):
        self.__lem = 0
        self.__sug = 0
        self.__cup = 0
        self.__pit = 0

        self.__open = '''

        <!DOCTYPE html>
        <html>
            <head>
                <title></title>
            <head>
        <body>
        '''
        self.__content = '''
                <p> ${self.total}</p>
                '''
        self.__close = '''

        </body>
        </html>
        '''

        self.__page = self.__open + self.__content+ self.__close

    def print_info(self):
        return self.__page

    @property
    def total(self):
        return self.__page

    @total.setter
    def total(self, total):
        self.__page = str(total)
        self.update()

    def update(self):
        self.__page = self.__page.format(**locals())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
