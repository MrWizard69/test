class HomePage(object):
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
        <div id="wrapper">
            <ul>
                <li><a href="?page1=a">Page1</a></li>
                <li><a href="?page2">Page2</a></li>
            </ul>
        </div>
        '''
        self.page_close = '''
    </body>
</html>
'''
    def print_out(self, content):
        #if the content.. is an empty string.. print the form
        #else.. print out the content
        return self.page_open + self.page_content + content + self.page_close
