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
            w_model = WeatherModel() #creates an instance of the model
            w_model.code = self.request.GET['code'] #pass url var into model
            w_model.send_req() #connect to API

            w_view = WeatherView() #the view that's going to show my info
            w_view.wdo = w_model.wdo #transfer wdo from model to view
            w_view.update() #creates html using our wdo data
            view.page_content = w_view.content #inserting weather view into form view

        self.response.write(view.print_out())

#weatherView
class WeatherView(object):
    ''' This class is showing Just the weather information from the API '''
    def __init__(self):
        self.wdo = WeatherDataObject()
        self.content = ''

    def update(self):
        self.content = '''
        <div>
            <h3>{self.wdo.location}</h3>
            <ul>
                <li><strong>Temperature: </strong>{self.wdo.temp}</li>
                <li><strong>Conditions: </strong>{self.wdo.condition}</li>
            </ul>
        </div>'''
        self.content = self.content.format(**locals())
        #print self.content

class WeatherModel(object):
    ''' This class handles data requests and sorting of data from API '''
    def __init__(self):
        self.url = 'http://xml.weather.yahoo.com/forecastrss?p='
        self.full_url = ''
        self.__code = ''
        #go get the api info
        '''
        Nodes:
            nested tags (aka tag pairs) -firstChild
            standalong tag- no firstChild needed
        '''

    def send_req(self):
        self.full_url = self.url + self.__code
        req = urllib2.Request(self.full_url)
        opener = urllib2.build_opener()
        data = opener.open(req)
        #parse it
        xmldoc = minidom.parse(data)
        #find the tag that we want.. and put that info into the wdo
        self.__wdo = WeatherDataObject() #create instance of data object class
        condition = xmldoc.getElementsByTagName('yweather:condition')
        self.__wdo.condition = condition[0].attributes['text'].value
        self.__wdo.temp = condition[0].attributes['temp'].value
        self.__wdo.code = condition[0].attributes['code'].value
        loc = xmldoc.getElementsByTagName('yweather:location')
        self.__wdo.location = loc[0].attributes['city'].value
        #print self.__wdo.location


    #don't want anyone overwriting my data object... so I'm making a property with jus a getter.
    @property
    def wdo(self):
        return self.__wdo


    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, c):
        self.__code = c

class WeatherDataObject(object):
    ''' this holds the information sent by the API'''
    def __init__(self):
        self.location = ''
        self.temp = ''
        self.condition = ''
        self.code = 0 #this code is the weather code (not the zip)




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
