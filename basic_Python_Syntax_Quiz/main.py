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
