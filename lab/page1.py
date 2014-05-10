class TellPage(object):
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
        <h1>Thank You!</h1>
        '''
        self.page_close = '''
    </body>
</html>
'''
    def print_out(self, content):
        #if the content.. is an empty string.. print the form
        #else.. print out the content
        return self.page_open + self.page_content + content + self.page_close

