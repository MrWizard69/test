'''
Multi-line comments
Jordan Wilson
5/5/14
DPW
'''
#This is where I collect the names of the characters
name1 = raw_input('Who is the first person? ')
money1 = 20
name2 = raw_input('Who is the second person?' )
money2 = 30
name3 = raw_input('Who is the third person? ')
money3 = 40
total1 = money1 + money2

people = [name1, money1, name2, money2, name3, money3]
#This is everyone name and how much money they have to spend
print "Here is everyone and their money: "
print people
#At the end of this line here is where the total1 variable shows up
message1 = '''{name1} was walking around and minding his own business. {name1} has {money1} in his wallet. One day,  {name1} saw a new video game. {name1}  saw that he did not have enough to buy it, so he called up his good friend {name2}. {name2} has {money2} in his wallet. Together they have {total1}.'''


message1 = message1.format(**locals())

print message1

message2 = '''{name3} recently bought a magazine with a bunch of nice stuff in it! There is both computers and software.'''
message2 = message2.format(**locals())
print message2

#This is where I collect the prices of the items from the users
comps = int(raw_input('How much is one of the computers? '))
soft = int(raw_input('How much one of the software '))
game = int(raw_input('How much is one of the games? '))

#This is the my dictionary and the two lines below it is where I display it
mag_info = {'Computers': comps, 'Software': soft, 'Games':game}

print mag_info['Games']
print 'is the same game that ' + name1 + ' ' + name2 + ' wants!'
print name3 + ' ' + ' would like to pool everyones money.'
total1 += money3
print total1
print 'is what they would all have if they all pooled their funds together.'

#If one
if money1>game:
    print name1 + ' can afford to buy it alone!'
else:
    print name1 + ' can not afford to buy it alone!'

#If two
if money2 + money3>game:
    print name2 + ' and ' + name3 + ' can afford to buy it together!'
else:
    print name2 + ' and ' + name3 + ' can not afford to buy it together!'

#A nice for loop
for i in range(1, 6, 2):
    print people[i] * 2

print 'is what' + ' ' + name1 + ', ' + name2 + ', ' + name3 + ' wish they had'
print 'one day the three of them got together. They wanted to come up with a complicated way to buy all three items in'
print 'the magazine. So they came up with this'

#This is one of my first complicated functions
def compli_calc(a,b,c):
    a = money1
    b = money2
    c = money3
    fair = a + b * c
    print name3 + ' owed everyone a favor...'
    print fair

compli_calc(money1,money2,money3)

print 'Not everyone thought that it was fair that someone had to pay so much, so a new calc was created!'
#Some felt the first complicated function wasn't fair so this one was made as a result
def compli_calcular(a,b,c):
    a = money1 * 2
    b = money2 * 2
    c = money3 / 2
    new_fair = a * b / c
    print 'This is how ' + name3 + ' felt the future money should be contributed.'
    return new_fair

new_new = compli_calcular(money1,money2,money3)

print new_new

