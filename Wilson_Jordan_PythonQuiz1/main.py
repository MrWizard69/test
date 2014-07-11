width = raw_input('Enter the width: ')
height = raw_input('Enter the height: ')

def calc_area(p1,p2):
    area = p1 * p2
    if p1 == p2:
        print 'It is a square!'
    else:
        print 'It is a rectangle!'
    return area

print calc_area(int(width),int(height))

booze = raw_input('How many bottles are on the wall? ')

for i in range(int(booze), 1, -1):
    print str(i) + ' bottles of beer on the wall'
    print 'take one down pass it around, now you have' + str(i - 1) + ' of beeeeeer!'
