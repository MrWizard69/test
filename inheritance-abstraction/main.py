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

#if self.request.GET['form'] == "deli"
#if not self.request.GET:
#plinks(content) = page()
#plinks.content
#elif self.request.GET['form'] =="deli"
#deli.form = formPage()
#elif self.request.GET['subs']
#subs.form = FormPage()

#content- deli meat, subs (links)
#<a href="?form=deli">deli meat</a>

# class animal
#traits
#method sounds()
#cobra
#eagle
#all sub classes to class animal

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.title = "Welcome All"
        p.form_header = "Enter your name:"
        p.css_url = "css/styles.css"
        self.response.write(p.print_out())

        p2 = FormPage()

class Page(object):
    def __init__(self):
        self._open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>{self.title}</title>
        <link rel="stylesheet" type="text/css" href="{self.css_url}" />
    </head>
    <body id="wrapper">'''
        self._content = 'This is my content'

        self._close = '''
    </body>
</html>'''
        self._css_url = ''
        self._title = ''
        self.all =''

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, t):
        self._title = t

    @property
    def css_url(self):
        return self._css_url

    @css_url.setter
    def css_url(self, c):
        self._css_url = c

    def print_out(self):
        self.update()
        return self.all

    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())


class FormPage(Page):
    def __init__(self):
        #call the constructor function of the parent
        Page.__init__(self)
        #super(FormPage, self).__init__()
        self.__form_open ='<form method="GET" action="">'
        self.__inputs ='''
    <input type="text" name="f_name" placeholder="First Name" />
    <input type="text" name="l_name" placeholder="Last Name" />
    <input type="submit" name="submit" />
    '''
        self.__form_close = '</form>'
        self.form_header = ">>Form Header<<"
        self._content = self.form_header + self.__form_open + self.__inputs + self.__form_close

    def update(self):
        self.all = self._open + self.form_header + self.__form_open + self.__inputs + self.__form_close + self._close
        self.all = self.all.format(**locals())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
