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
        c = Cow()
        d = Duck()
        f = Fox()
        p.title = "Welcome!"
        c.title = 'Cow'
        d.title = 'Duck'
        f.title = 'Fox'
        ani = [c, d, f] #the animal array

        if self.request.GET:
            animal = self.request.GET['an']

            if animal == "c":
                self.response.write(ani[0].print_out())
            elif animal == "d":
                self.response.write(ani[1].print_out())
            elif animal == "f":
                self.response.write(ani[2].print_out())
        else:
            self.response.write(p.print_out())





class PageBuilder(object): #the html page
    def __init__(self):
        self.open = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>{self.title}</title>
            <link href="css/styles.css" rel="stylesheet" type="text/css"
            <link href='http://fonts.googleapis.com/css?family=Droid+Sans' rel='stylesheet' type='text/css'>
        </head>
        <body>
        '''
        self.close = '''</body></html>'''
        self.content = '''
        <div id="wrapper">
        <h1>{self.title}</h1>
        <ul>
            <li><a href="?an=c">Cow</a></li>
            <li><a href="?an=d">Duck</a></li>
            <li><a href="?an=f">Fox</a></li>
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
        <p>Cow goes moo and ducks go quack quack. But there's one sound that no one knows... WHAT DOES THE FOX SAY?</p>
        </div>
        '''
        self.all = ''''''

        self.phylum = "" #place holders for the information
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
            cow.phylum = "Phylum: Chordate"
            cow.a_class = " Class: Mammalia"
            cow.order = "Order: Artiodactyla"
            cow.family = " Family: Bovidae"
            cow.genus = "Genus: Bos Taurus"
            cow.url = "<img src='images/cow.jpg' alt='cow'>"
            cow.life = "Lifespan: 15 Years"
            cow.habitat = "Habitat: Grasslands and Forests"
            cow.geolocation = "Geolocation: On Farms Everywhere"
            cow.sound = "Sound: MEROOOOO"

            self.gather(cow)

class Duck(Animal):
        def __init__(self):
            Animal.__init__(self)
            duck = Animal()
            duck.phylum = "Phylum: Chordata"
            duck.a_class = "Class: Aves"
            duck.order = "Order: Anseriformes"
            duck.family = "Family: Anatidae"
            duck.genus = "Genus: Duck"
            duck.url = "<img src='images/duck.jpg' alt='duck'>"
            duck.life = "Lifespan: 4 - 8 years"
            duck.habitat = "Habitat: Rivers, lakes and woodland wetlands"
            duck.geolocation = "Geolocation: At a pond near you!"
            duck.sound = "Sound: QUACK!"

            self.gather(duck)

class Fox(Animal):
        def __init__(self):
            Animal.__init__(self)
            fox = Animal()
            fox.phylum = "Phylum: Chordata"
            fox.a_class = "Class: Mammalia"
            fox.order = "Order: Carnivora"
            fox.family = "Family: Canidae"
            fox.genus = "Genus: Canis"
            fox.url = "<img src='images/fox.jpg' alt='fox'>"
            fox.life = "Lifespan: 5 Years"
            fox.habitat = "Habitat: The northern hemisphere from the Arctic Circle to North Africa, and Central America."
            fox.geolocation = "Geolocation: Everywhere"
            fox.sound = "Sound: Ring-ding-ding-ding-dingeringeding!"

            self.gather(fox)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
