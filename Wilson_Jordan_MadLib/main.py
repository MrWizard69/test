'''
Multi-line comments
Jordan Wilson
5/5/14
DPW
'''

name1 = raw_input('Who is the first person?')
money1 = 20
name2 = raw_input('Who is the second person?')
money2 = 30
name3 = raw_input('Who is the third person?')
money3 = 40
total1 = money1 + money2

people = [name1, money1, name2, money2, name3, money3]

print "Here is everyone and their money: "
print people

message1 = '''{name1} was walking around and minding his own business. {name1} has {money1} in his wallet. One day,  {name1} saw a new video game. {name1}  saw that he did not have enough to buy it, so he called up his good friend {name2}. {name2} has {money2} in his wallet. Together they have {total1}.'''


message1 = message1.format(**locals())

print message1

message2 = '''{name3} recently bought a magazine with a bunch of nice stuff in it! There is both computers and software.'''
message2 = message2.format(**locals())
print message2
comps = int(raw_input('How much is one of the computers?'))
soft = int(raw_input('How much one of the software'))
game = int(raw_input('How much is one of the games?'))

mag_info = {'Computers': comps, 'Software': soft, 'Games':game}

print mag_info['Games']
print 'is the same game that ' + name1 + ' ' + name2 + ' wants!'
print name3 + ' ' + ' would like to pool everyones money.'
total1 += money3
print total1 + ' is what they would all have if they all pooled their funds together.'

if money1>soft:
    print 'comps win!'
else:
    print 'soft win!'
