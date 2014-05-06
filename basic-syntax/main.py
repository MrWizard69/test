#single line comments!
'''
Multi-line comments
Jordan Wilson
5/5/14
DPW
'''

print "Hello World!"

first_name = 'Kermit '
last_name = 'Da Frog'

print first_name + last_name

year_born = 1990
year_born += 1
age = 2014 - year_born
print age
print year_born

# assignment operators += -= *= /= they assign values to variables

'''
if(year_born < 1990){
    print 'You are part of generation Y'
}
'''

if year_born < 1995:
    print 'You are part of the millennial generation'
elif year_born > 1978:
    print 'You are part of generation Y'
elif year_born > 1965:
    print 'you are part of generation X'
    #pass - tells python to move along. it's for setting up basic if else structure.

print 'this is outside of the conditional statement'

#array
students = ['Nicole','Eli', 'Gabriel', 'Jordan', 'Danny']
print students
students.append('Arturo')
print students

#dictionaries - associative arrays
#name_of_dict = {'key': value}
class_info = {'students': students, 'roster count': 9, 'room':'FS4A107'}
print class_info['roster count']
print class_info

#loops
'''
for s in students:
    print s + ', you will do great in this class!'

'''

#for in in range(start, end, inc/dec)
for i in range(0,5, 1):
    print students[i]

#for i in range(0, 10, 2):
    #print i

import random

for i in range(0, 10):
    print random.randrange(20)

#function
def calc_area():
    area = 200 * 300
    return area

a = calc_area()
print a

def calc_area1():
    area = 3 * 6
    print area

calc_area1()

#format string method
user_name = 'Kermit'
join_date = 2001
message = '''
Welcome to our site, {user_name}! It's great you are here! You've been with us since {join_date}!
'''

message = message.format(**locals())
print message

#getting info from the user
first_name = raw_input('Type your first Name: ')
age = raw_input('Type your age: ')
print first_name + ", nice to meet you."
print int(age)
print str(int(age)) + " is your age..."