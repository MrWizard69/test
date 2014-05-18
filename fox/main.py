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
        p = PageBuilder()
        o1 = Cow()
        o2 = Duck()
        o3 = Fox()
        p.title = "Welcome!"
        o1.title = 'Object1'
        o2.title = 'Object2'
        o3.title = 'Object3'
        ani = [ o1, o2, o3]

        if self.request.GET:
            animal = self.request.GET['an']

            if animal == "o1":
                self.response.write(ani[0].print_out())
            elif animal == "o2":
                self.response.write(ani[1].print_out())
            elif animal == "o3":
                self.response.write(ani[2].print_out())
        else:
            self.response.write(p.print_out())





class PageBuilder(object):
    def __init__(self):
        self.open = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>{self.title}</title>
        </head>
        <body>
        '''
        self.close = '''</body></html>'''
        self.content = '''
        <ul>
            <li><a href="?an=o1">Object1</a></li>
            <li><a href="?an=o2">Object2</a></li>
            <li><a href="?an=o3">Object3</a></li>
        </ul>
        <p>{self.phylum}</p>
        <p>{self.a_class}</p>
        <p>{self.order}</p>
        <p>{self.family}</p>
        <p>{self.genus}</p>
        <p>{self.url}</p>
        <p>{self.life}</p>
        <p>{self.habitat}</p>
        <p>{self.geolocation}</p>
        <p>{self.sound}</p>
        Content goes here
        '''
        self.all = ''''''

        self.phylum = ""
        self.a_class = ""
        self.order = ""
        self.family = ""
        self.genus = ""
        self.url = ""
        self.life = ""
        self.habitat = ""
        self.geolocation = ""
        self.sound = ""

    def print_out(self):
        self.update()
        return self.all

    def update(self):
        self.all = self.open + self.content + self.close
        self.all = self.all.format(**locals())

class Animal(PageBuilder):
    def __init__(self):
        PageBuilder.__init__(self)

    def gather(self, content):
        self.phylum = content.phylum
        self.a_class = content.a_class
        self.order = content.order
        self.family = content.family
        self.genus = content.genus
        self.url = content.url
        self.life = content.life
        self.habitat = content.habitat
        self.geolocation = content.geolocation
        self.sound = content.sound


class Cow(Animal):
        def __init__(self):
            Animal.__init__(self)
            cow = Animal()
            cow.phylum = "1"
            cow.a_class = "2"
            cow.order = "3"
            cow.family = "3"
            cow.genus = "4"
            cow.url = "5"
            cow.life = "6"
            cow.habitat = "7"
            cow.geolocation = "8"
            cow.sound = "Sound1"

            self.gather(cow)

class Duck(Animal):
        def __init__(self):
            Animal.__init__(self)
            duck = Animal()
            duck.phylum = "9"
            duck.a_class = "10"
            duck.order = "11"
            duck.family = "12"
            duck.genus = "13"
            duck.url = "14"
            duck.life = "15"
            duck.habitat = "16"
            duck.geolocation = "17"
            duck.sound = "Sound2"

            self.gather(duck)

class Fox(Animal):
        def __init__(self):
            Animal.__init__(self)
            fox = Animal()
            fox.phylum = "18"
            fox.a_class = "19"
            fox.order = "20"
            fox.family = "21"
            fox.genus = "22"
            fox.url = "23"
            fox.life = "24"
            fox.habitat = "25"
            fox.geolocation = "26"
            fox.sound = "Sound3"

            self.gather(fox)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
