class Page():
    def __init__(self):
        self.header = '''
<!DOCTYPE html>
<html>
    <head>
        <title>Lab 3</title>
    </head>
    <body>
        '''
        self.content = '''
            Content
            '''
        self.closer = '''
    </body>
</html>
        '''

    def print_out(self):
        return self.header + self.content + self.closer