'''
Jordan Wilson
6/08/14
Day1
'''

print "Amazing! :D"
print "It Works!!!"

first_name = "Jordan"
last_name = "Wilson"
print first_name + ' ' + last_name
year_born = 1990
age = 2014 - year_born
print age
print "I am " + str(age) + " years old"

new_age= raw_input("Type your age: ") #collects info as strings
print "You are " + new_age + " years old"

budget = 200
shoe_price = 60
won_lottery = True
if shoe_price <= budget:
    print "I can buy my shoooooz!"
    #pass
elif won_lottery:
    print "By da shooooz!"
else:
    print "No shoes for you!"
print "I am done with code! :D"


#functions
def calc_area(w,h):
    a = w * h
    return a
area = calc_area(50,60)
print str(area) + " sqft"

#Loops & Arrays

for i in range(0,5):
    print i

for i in range(5,0,-1):
    print i

for i in range(0,5,2):
    print i

students = ['Studnicky', 'Julian', 'Seth', 'Jordan', 'Danny', 'Carmine', 'Manny']
students.append("Alan")

for s in students:
    print s

i = 0
while i < 5:
    print i
    i += 1

#Dictionaries
obj = {"name":"Jordan", "age":"23", "occupation":"student"}
print obj["name"]

big_string = '''
    Welcome to the Python class, {user_name}. You are going to do so well in this class!!!
'''
#string that goes to the next line
user_name = "Mr.Wizard69"
print big_string.format(**locals())
