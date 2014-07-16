import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        if self.request.GET: #this is where the info from the input boxes are called
            p.content = "<h1>Thank You For Signing Up!</h1>"
            # if self.request.GET.has_key[news]
            #     self.request.GET['news'] = 'No'
            p.content += "<div class='form'>"
            p.content += "<p>Please keep this information for safe keeping.</p>"
            p.content += "<p>Full Name: " + self.request.GET['flname'] + "</p>"
            p.content += "<p>your email: " + self.request.GET['email'] + "</p>"
            p.content += "<p>Username: " + self.request.GET['user'] + "</p>"
            p.content += "<p>Password: " + self.request.GET['pass'] + "</p>"
            p.content += "<p>Your Favorite Console: " + self.request.GET['console'] + "</p>"
            #p.content += "<p>News?: " + self.request.GET['news'] + "</p>"
            p.content += "</div>"

            self.response.write(p.print_out_page())
        else:
            self.response.write(p.print_out_form()) #if not, then go to the form page

class Page(object): #this is the template for the two pages
    header = '''<!DOCTYPE>
<html>
    <head>
        <link rel="stylesheet" href="css/styles.css" type="text/css" />
        <link href='http://fonts.googleapis.com/css?family=Share+Tech+Mono' rel='stylesheet' type='text/css'>
        <title>Simple Form</title>
    </head>
    <body>
    <nav id="nav"><ul>
		<li>| <a href="#">Games</a></li>
		<li>| <a href="#">Login</a> |</li>
		<li><a class="select" href="http://localhost:9080/">Sign Up</a>| </li>
	</ul></nav>
    '''
    content = '''Hello there''' #page 2
    form_content = '''
        <h1>Welcome to Play-Free-Web-Games! :D</h1>
        <h3>Sign Up</h3>
        <div class="form">
        <p>Please fill out this form to start playing for free!</p>
        <form method="GET">
            <input type="text" placeholder="Full Name" name="flname" />
            <input type="text" placeholder="Email" name="email" />
            <input type="text" placeholder="Username" name="user" />
            <input type="text" placeholder="Password" name="pass" />
             <p>Choose your favorite console</p>
             <select name="console">
                <option value="XBox">XBox</option>
                <option value="Playstation">Playstation</option>
                <option value="Nintendo">Nintendo</option>
            </select>
            <br /><input type="checkbox" name="news" value="Yes" /> Sign Up for the News Letter? <br />
            <input type="submit" value="Submit" />
        </form>
        </div>
    '''# page 1 ^
    closer = '''
    </body>
    </html>'''

    def print_out_page(self): #this is where the specific pieces of the pages are printed out
        return self.header + self.content + self.closer

    def print_out_form(self):
        return self.header + self.form_content + self.closer

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
