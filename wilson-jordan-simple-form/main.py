import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        if self.request.GET:
            p.content = "<p>Please keep this information for safe keeping.</p>"
            p.content += "<p>First Name: " + self.request.GET['fname'] + "</p>"
            p.content += "<br /><p> Last Name: " + self.request.GET['lname'] + "</p>"
            self.response.write(p.print_out_page())
        else:
            self.response.write(p.print_out_form())

class Page(object):
    header = '''<!DOCTYPE>
<html>
    <head>
        <link rel="stylesheet" href="css/styles.css" type="text/css" />
        <title>New Page</title>
    </head>
    <body>
    <nav id="nav"><ul>
		<li>| <a href="#">Games</a></li>
		<li>| <a href="#">Login</a> |</li>
		<li class="select"><a href="http://localhost:9080/">Sign Up</a>| </li>
	</ul></nav>
    '''
    content = '''Hello there'''
    form_content = '''
        <h1>Welcome to Play-Free-Web-Games! :D</h1>
        <h3>Sign Up</h3>
        <p>Please fill out this form to start playing for free!</p>
        <form method="GET">
            <input type="text" placeholder="First Name" name="fname" />
            <input type="text" placeholder="Last Name" name="lname" />
            <input type="submit" value="Submit Info" />
        </form>
    '''
    closer = '''
    </body>
    </html>'''

    def print_out_page(self):
        return self.header + self.content + self.closer

    def print_out_form(self):
        return self.header + self.form_content + self.closer

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
