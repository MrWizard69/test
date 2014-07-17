class Page():
    def __init__(self):
        #This is what is displayed first
        self.header = '''
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="css/styles.css" type="text/css" />
        <link href='http://fonts.googleapis.com/css?family=Share+Tech+Mono' rel='stylesheet' type='text/css'>
        <title>Lab 3</title>
    </head>
    <body>
        '''
        self.content = '''
            <div id="nav">
                <ul>
                    <li>|<a href="?game=0">FIFA World Cup Brazil 2014</a>|</li>
                    <li><a href="?game=1">Destiny</a>|</li>
                    <li><a href="?game=2">Titanfall</a>|</li>
                    <li><a href="?game=3">Minecraft</a>|</li>
                    <li><a href="?game=4">Grand Theft Auto V</a>|</li>
                </ul>
            </div>

            <h1>Go Ahead and browse the top 5 most popular Xbox games</h1>
            '''
        self.closer = '''
        <footer><a href="http://localhost:11080/">Refresh The Page</a></footer>
    </body>
</html>
        '''

    def print_out(self): #displayes everything above.
        return self.header + self.content + self.closer