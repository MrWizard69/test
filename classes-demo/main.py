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

width = int(raw_input("What is the width? "))
height = int(raw_input("What is the height? "))

def calc_area(): #this is calculate area and tell the user if they are making a square or rectangle

    area = width * height
    if width == height:
        print "This is a square"
    else:
        print "This is a rectangle"
    return area

print calc_area() #this is where it's spit out

beer = int(raw_input("How much beer is on the wall? "))
def count_down(beer): # this will play the beer song
    for i in range(beer, 1, -1):
        print str(i) +" bottles of beer on the wall!" #this is where the beers number is displayed
        print "Now you have " + str(i - 1) + " bottles of beer on the wall!" #this is where the next beer number is displayed
print count_down(beer)