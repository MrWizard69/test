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
        o1 = Object1()
        o2 = Object2()
        o3 = Object3()
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


class Object1(Animal):
        def __init__(self):
            Animal.__init__(self)
            object1 = Animal()
            object1.phylum = "1"
            object1.a_class = "2"
            object1.order = "3"
            object1.family = "3"
            object1.genus = "4"
            object1.url = "5"
            object1.life = "6"
            object1.habitat = "7"
            object1.geolocation = "8"
            object1.sound = "Sound1"

            self.gather(object1)

class Object2(Animal):
        def __init__(self):
            Animal.__init__(self)
            object2 = Animal()
            object2.phylum = "9"
            object2.a_class = "10"
            object2.order = "11"
            object2.family = "12"
            object2.genus = "13"
            object2.url = "14"
            object2.life = "15"
            object2.habitat = "16"
            object2.geolocation = "17"
            object2.sound = "Sound2"

            self.gather(object2)

class Object3(Animal):
        def __init__(self):
            Animal.__init__(self)
            object3 = Animal()
            object3.phylum = "18"
            object3.a_class = "19"
            object3.order = "20"
            object3.family = "21"
            object3.genus = "22"
            object3.url = "23"
            object3.life = "24"
            object3.habitat = "25"
            object3.geolocation = "26"
            object3.sound = "Sound3"

            self.gather(object3)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
