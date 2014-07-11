width = raw_input('Enter the width: ') #collecting users width
height = raw_input('Enter the height: ') #colecting users height

def calc_area(p1,p2): #the function that calcs the area
    area = p1 * p2
    if p1 == p2:
        print 'It is a square!' #if the width and height is == then it's a square
    else:
        print 'It is a rectangle!' #if the width and height is != then it's a rectangle
    return area

print calc_area(int(width),int(height)) #displaying the area

booze = raw_input('How many bottles are on the wall? ') #ALL the booze
def count_down(booze):
    for i in range(int(booze), 0, -1): #the count down
        print str(i) + ' bottles of beer on the wall' #number of beer
        print 'take one down pass it around, now you have ' + str(i - 1) + ' bottles of beeeeeer!' #number of beer - 1

print count_down(booze) #printing out the loop
