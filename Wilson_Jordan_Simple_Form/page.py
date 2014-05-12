class HTMLPage(object):
    def __init__(self): #constructor
        self.page_open = '''

<!DOCTYPE html>
<html>
    <head>
        <title>BUY A NEW CAR!</title>
        <link href="css/styles.css" rel="stylesheet" type="text/css"
        <link href='http://fonts.googleapis.com/css?family=Droid+Sans' rel='stylesheet' type='text/css'>
    </head>
    <body>
        '''
        self.page_content = '''
        <h1>Pick Up Your New Car Today!</h1>
    <form method="GET" action="" id="wrapper">
        <input type="text" name="firstname" placeholder="First Name" />
        <input type="text" name="lastname" placeholder="Last Name" />
        <input type="text" name="cardnumber" placeholder="Credit Card Number" />
        <input type="checkbox" name="resident" value="FL" />Are you a florida resident?

        <select name="car">
            <option value="Volvo">Volvo</option>
            <option value="Saab">Saab</option>
            <option value="Mercedes">Mercedes</option>
            <option value="Audi">Audi</option>
        </select>

        <input type="submit" name="submit" value="go" />
        <p>You can always trust us! ;D</p>
    </form>
        '''
        self.page_close = '''
    </body>
</html>
'''
    def print_out(self, content):
        #if the content.. is an empty string.. print the form
        #else.. print out the content
        return self.page_open + self.page_content + content + self.page_close
