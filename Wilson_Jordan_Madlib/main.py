#Jordan Wilson
#07/08/14
#Madlib

noun = raw_input("Enter a noun: ") #a variable that stores user input
verb = raw_input("Enter a verb: ") #a variable that stores user input
num1 = raw_input("Enter a number between 1-7: ")
if int(num1) > 7 or int(num1) < 1:
    print "Your number is not within the proper range"
    num1 = input("Enter a number between 1-7: ")

num2 = raw_input("Enter another number: ")
people = ['Jordan', 'Andrew', 'Kyle', 'Blair', 'Justin', 'Forrest', 'Missy']

def enemy_calc(p1,p2):
    r = int(num2) / int(num1) + p1 + p2
    return r
result = enemy_calc(int(num1), int(num2))
#print result



wizard = {"name":"Mr.Wizard", "age":"33", "occupation":"Wizard"}
#print wizard["name"]

print wizard["name"] + " has his back up against the wall against his rival RL!"
raw_input()
print wizard["name"] + "'s wand broke. He reached into his robe and out of desparation, he pulled out a " + noun + "!"
raw_input()
print "He knew this wasn't conventional, but it could work."
raw_input()
print "RL casted a crippling spell! The light the spell emitted was flashing wildly!"
raw_input()
print wizard["name"] + " quickly dodged it and countered with a spell of his own. The spell " + verb + " toward RL!"
raw_input()
print "RL laughed at the attempt and deflected " + wizard["name"] + " spell."
raw_input()
print '"It appears that we are evenly matched" RL said. "Good thing I brought my friends..."'
raw_input()
print str(result) + " dark wizards busted into the room!"
raw_input()
print wizard["name"] + ' smirked and said, "Good thing I brought some friends of my own!"'
raw_input()
print "Just then..."
raw_input()
for i in people:
    print i
print "Came into the room wands ready."
raw_input()
print "The room became quiet. The air heavy."
raw_input()
print "The tension of what was to come filled the room. The final duel has begun."
raw_input()
print "To be continued... :D"
