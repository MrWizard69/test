import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
        #instance = Class()
        yoda = Character()#create instance
        yoda.name = "Jedi Master Yoda"
        yoda.occupation = "Jedi Knight"
        yoda.hometown = "Dagoba"
        yoda.quote = "Anger leads to hate.. hate leads to fear.."
        self.response.write(yoda.say())

        leia = Character()
        leia.name = "Princess Leia Organa"
        leia.Occupation = "Princess, General of the Rebel Forces"
        leia.hometown = "Alderan"
        leia.quote = "You're me only hope"
        self.response.write(leia.say())

class Character(object):
    def __init__(self):
        self.name = ""
        self.occupation = ""
        self.age = 0
        self.hometown = ""
        self.quote = ""
    def fight(self):
        print "AHA! Fight You!!!"

    def say(self):
        print self.quote
        return self.quote

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

