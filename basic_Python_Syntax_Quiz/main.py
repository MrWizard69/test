def calc_area():
    width = 10
    height = 10
    area = width * height
    if width == height:
        print "This is a square"
    else:
        print "This is a rectangle"
    return area

print calc_area()

beer = 99
def count_down(beer):
    for i in range(beer, 1, -1):
        print str(i) +" bottles of beer on the wall!"
        print "Now you have " + str(i - 1) + " bottles of beer on the wall!"
print count_down(beer)