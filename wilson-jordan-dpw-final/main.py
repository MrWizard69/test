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
from page import FormPage
from xml.dom import minidom
import urllib2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        view = FormPage()
        view.form_header = 'string'

        if self.request.GET:
            code = self.request.GET['code']
            w_model = Model()
            w_model.code = self.request.GET['code']
            #w_model.send_req()
            w_view = View()
            #w_view.wdo = w_model.wdo
            w_view.update()
            view.page_content = w_view.content

        self.response.write(view.print_out())

class View(object):
    def __init__(self):
        wdo = DataObject()
        self.content = ''

    def update(self):
        self.content = '''
        <h1>{self.wdo.name}</h1>
        <p>{self.wdo.sigil}</p>
        <p>{self.wdo.motto}</p>'''

        self.content = self.content.format(**locals())

class Model(object):
    def __init__(self):
        self.url = 'http://rebeccacarroll.com/api/got/got.xml'
        self.full_url = self.url + self.__code
        req = urllib2.Request(self.full_url)
        opener = urllib2.build_opener()
        data = opener.open(req)
        xmldoc = minidom.parse(data)
        self.__wdo = DataObject()
        name = xmldoc.getElementsByTagName('name').firstChild.NodeValue
        sigil = xmldoc.getElementsByTagName('sigil').firstChild.NodeValue
        motto = xmldoc.getElementsByTagName('motto').firstChild.NodeValue
        self.__wdo.code = name[0].attributes['code']

        @property
        def wdo(self):
            return self.__wdo

        @property
        def code(self):
            return self.__code

        @code.setter
        def code(self, c):
            self.__code = c

class DataObject(object):
    def __init__(self):
        self.name = ''
        self.sigil = ''
        self.motto = ''


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
