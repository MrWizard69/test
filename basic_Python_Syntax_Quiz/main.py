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