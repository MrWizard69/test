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
            <div>
                <ul>
                    <li><a href="?game=1">FIFA World Cup Brazil 2014</a></li>
                    <li><a href="?game=2">Destiny</a></li>
                    <li><a href="?game=3">Titanfall</a></li>
                    <li><a href="?game=4">Minecraft</a></li>
                    <li><a href="?game=5">Grand Theft Auto V</a></li>
                </ul>
            </div>
            '''
        self.closer = '''
    </body>
</html>
        '''

    def print_out(self):
        return self.header + self.content + self.closer