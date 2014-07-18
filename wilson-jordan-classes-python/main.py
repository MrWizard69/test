import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

        self.new_student = Student()
        self.new_student.name = 'John'
        self.new_student.age = 23
        self.new_student.edu = 'Web Dev'
        self.new_student.money = 20000
        self.new_student.gpa = 3.0
        self.new_student.gpa_saver()


        self.poorjoe = Custodian
        self.poorjoe.name = 'Joe'
        self.poorjoe.age = 46
        self.poorjoe.money = 30000
        self.poorjoe.employed = 10
        self.poorjoe.toiletscleaned = 5
        self.poorjoe.money_adder(self)

        self.guy = Sports_Car()
        self.guy.driver = 'Guy'
        self.guy.mgp = 45
        self.guy.tires = 4
        self.guy.cyl = 6
        self.guy.raceswon = 0
        self.guy.win(10)
    

class Student(object):
    def __init__(self):
        self.name = ''
        self.__age = 0
        self.edu = ''
        self.__money = 0
        self.gpa = 0


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, a):
        self.__age = a

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, m):
        self.__money = m


    def gpa_saver(self):
        newgpa = self.gpa + 1
        return newgpa #this method saves a failing gpa



class Custodian(object):
    def __init__(self):
        self.name = ''
        self.age = 0
        self.__money = 0
        self.employed = 0
        self.__toiletscleaned = 0

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, m):
        self.__money = m

    @property
    def toiletscleaned(self):
        return self.__toiletscleaned

    @toiletscleaned.setter
    def toiletscleaned(self, t):
        self.__toiletscleaned = t

    def money_adder(self):
        payday = self.money + 60000
        return payday #this method makes sure we all get what we deserve!

class Sports_Car(object):
    def __init__(self):
        self.driver = ''
        self.__mpg = 0
        self.tires = 0
        self.__cyl = 0
        self.raceswon = 0

    @property
    def mpg(self):
        return self.__mpg

    @mpg.setter
    def mgp(self, m):
        self.__mpg = m

    @property
    def cyl(self):
        return self.__cyl

    @cyl.setter
    def cyl(self, c):
        self.__cyl = c

    def win(self, w):
        winstreak = self.raceswon + w
        return winstreak #this method shows us that even losers can be winners, sometimes ;]





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
