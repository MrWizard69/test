#Jordan Wilson
#07/08/14
#Madlib

noun = raw_input("Enter a noun: ")
verb = raw_input("Enter a verb: ")
num1 = raw_input("Enter a number between 1-7: ")
if int(num1) > 7 or int(num1) < 1:
    print "Your number is not within the proper range"
    num1 = input("Enter a number between 1-7: ")

num2 = raw_input("Enter another number: ")
people = ['Jordan', 'Mr.Wizard', 'Kyle', 'Blair', 'Justin', 'Forrest', 'Missy']

def happy_calc(p1,p2):
    r = int(num2) / int(num1) + p1 + p2
    return r
result = happy_calc(int(num1), int(num2))
print result

for i in people:
    print i

wizard = {"name":"Mr.Wizard", "age":"33", "occupation":"Wizard"}
print wizard["name"]
