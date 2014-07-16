import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #YOU CAN"T USE self.response or self.request
        #both attributes of your MainHandler class
        p = Page() #creating an instance "p" of class Page
        #self.response.write('OMG STAHP!!!!')
        #self.response.write(p.print_out_form())
        if self.request.GET: #ONLY DO THIS IF THE FORM HAS DATA
            #changing the fontent in page
            p.content = "First Name: " + self.request.GET['fname']
            p.content += "<br /> Last Name: " + self.request.GET['lname']
            #printing out the page (without the form stuff)
            self.response.write(p.print_out_page())
        else:
            self.response.write(p.print_out_form())

class Page(object):
    header = '''<!DOCTYPE>
<html>
    <head>
        <link rel="stylesheet" href="css/styles.css" type="text/css" />
        <title>Welcome to My Page</title>
    </head>
    <body>
    '''
    content = '''Hello there'''
    form_content = '''
        <form method="GET">
            <input type="text" placeholder="First Name" name="fname" />
            <input type="text" placeholder="Last Name" name="lname" />
            <input type="submit" value="Submit Info" />
        </form>
    '''
    closer = '''
    </body>
    </html>'''

    def __init__(self):
        pass

    def print_out_page(self):
        return self.header + self.content + self.closer

    def print_out_form(self):
        return self.header + self.form_content + self.closer

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
