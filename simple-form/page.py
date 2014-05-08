class HTMLPage(object):
    def __init__(self): #constructor
        self.page_open = '''

<!DOCTYPE html>
<html>
    <head>
        <title>Welcome to my page</title>
        <link href="css/styles.css" rel="stylesheet" type="text/css"
    </head>
    <body>
        '''
        self.page_content = '''
    <form method="GET" action="">
        <input type="text" name="firstname" placeholder="First Name" />
        <input type="text" name="lastname" placeholder="Last Name" />
        <input type="submit" name="submit" value="go" />
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
