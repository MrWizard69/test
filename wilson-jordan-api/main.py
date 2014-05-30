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
        view.form_header = "NYT App"


        #if there are url variables...
        if self.request.GET:
            code = self.request.GET['code']
            w_model = nytModel() #creates an instance of the model
            w_model.code = self.request.GET['code'] #pass url var into model
            w_model.send_req() #connect to API

            w_view = nytView() #the view that's going to show my info
            #w_view.wdo = w_model.wdo #transfer wdo from model to view
            w_view.articles = w_model.articles
            w_view.update() #creates html using our wdo data
            view.page_content = w_view.content #inserting weather view into form view

        self.response.write(view.print_out())

#weatherView
class nytView(object):
    ''' This class is showing Just the weather information from the API '''
    def __init__(self):
        self.wdo = nytDataObject()
        self.content = ''

        #print self.wdo
        # print self.wdo.articles
    def update(self):
        for news in range(0,20):
             self.content += '''
             <div class="wrapper">
             <h1>''' + self.articles[news].title + '''</h1>
             <p>''' + self.articles[news].abstract + '''</p><img src="''' + self.articles[news].pic + '''" />
             <a href="''' + self.articles[news].link + '''">Read More...</a>
             </div>
            '''
        # self.content = self.content.format(**locals())
        #print self.content

class nytModel(object):
    ''' This class handles data requests and sorting of data from API '''
    def __init__(self):
        self.articles = []
        #go get the api info
        '''
        Nodes:
            nested tags (aka tag pairs) -firstChild
            standalong tag- no firstChild needed
        '''

    def send_req(self):
        url = 'http://api.nytimes.com/svc/news/v3/content/' + self.code + '/all/.xml?api-key=82768f8a5c54cdac403a515021a90c84:10:69415137'
        req = urllib2.Request(url)
        opener = urllib2.build_opener()
        data = opener.open(req)
        #parse it
        xmldoc = minidom.parse(data)
        #find the tag that we want.. and put that info into the wdo

       # self.__wdo.articles = []

        news = xmldoc.getElementsByTagName('news_item')



        for item in news:

            type(item.getElementsByTagName('title'))
            article = nytDataObject() #create instance of data object class
            article.title = item.getElementsByTagName('title')[0].firstChild.nodeValue
            article.abstract = item.getElementsByTagName('abstract')[0].firstChild.nodeValue
            article.link = item.getElementsByTagName('url')[0].firstChild.nodeValue

            if item.getElementsByTagName('thumbnail_standard')[0] and item.getElementsByTagName('thumbnail_standard')[0].firstChild:
                article.pic = item.getElementsByTagName('thumbnail_standard')[0].firstChild.nodeValue
                protocol = article.pic[0] + article.pic[1] + article.pic[2] + article.pic[3]
                if protocol != 'http':
                    article.pic = 'http://graphics8.nytimes.com/' + article.pic

            self.articles.append(article)

        #print self.__wdo.articles[0].firstChild.nodeValue
        # print self.articles[1]
        # print self.articles[2]


        #
        # for title in titles:
        #     self.articles.append(title.firstChild.nodeValue)
        #
        # self.abs = []
        # for abstract in abstracts:
        #     self.abs.append(abstract.firstChild.nodeValue)

        # self.links = []
        # for n in news:
        #     print '------------------------'
        #     print n.getElementsByTagName('url')[0].firstChild.nodeValue
        #     print '------------------------'

        # for urls in urlss:
        #     self.links.append(urls.firstChild.nodeValue)






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

class nytDataObject(object):
    ''' this holds the information sent by the API'''
    def __init__(self):
        self.title = ''
        self.abstract = ''
        self.urls = ''
        self.pic = ''
        self.articles = []





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
