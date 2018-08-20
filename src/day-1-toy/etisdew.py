import sys
import os
import datetime
import calendar

class Etisdew:
    def __init__(self):
        self.print('hello:', 'Hello World!')
        out = str(self.pow(2,65536))
        self.print('bignum (trunc.):', f'{out[0:5]}...{out[-5:]}')
        self.print('datatypes:', self.duckmath(5, '7', '+'), self.duckmath(5, 7, '+', True))
        v = sys.version_info
        self.print('modules:', f'PLATFORM={sys.platform}', 'PYTHON={}.{}.{}'.format(*v), f'PID={os.getpid()}', f'CWD={os.getcwd()}', f'USER={os.getlogin()}')
        x = 10
        y = 2.24552
        z = "\"I like turtles!\""
        self.print('printf:', 'x is %s, y is %s, x is %s' % (x, y, z), 'x is {}, y is {}, x is {}'.format(x, y, z))
        self.print('lists:')
        x = [1,2,3]
        y = [8,9,10]
        self.listexample(x, y)
        t = (1,2,5,7,99)
        tup = (1,)
        self.print('tuples:')
        self.print_tuple(*t)
        self.print_tuple(*tup)
        a = [2,4,1,7,9,6]
        s = "Hello, world!"
        self.print('slice:')
        self.sliceexample(a, s)
        self.print('comp:')
        self.compexample()
        self.print('dicts:')
        self.dictexample()
        self.print('func:')
        self.print('    ', self.funcexample())
        self.print('args:')
        self.argsexample()
        self.print('scope:')
        self.scopeexample()
        self.print('fileio:')
        self.fileioexample()
        self.print('cal:')
        self.calexample()
        self.print('class:')
        self.classexample()
    @staticmethod
    def print(*args, ):
        '''Print Hello World'''
        w = sys.stdout.write
        end = len(args) - 1
        for i, v in enumerate(args):
            if (i == end):
                w(f'{v}\n')
            else:
                w(f'{v} ')

    @staticmethod
    def pow(value, power, modulo = 0):
        '''Print out 2 to the 65536th power'''
        m = Etisdew.duckmath
        if modulo == 0 or power < 0:
            return m(value, power, '**')
        else:
            return m(m(value, power, '**'), modulo, '//')

    @staticmethod
    def duckmath(a, b, op, literal = False):
        if literal == False:
            a = int(a)
            b = int(b)
            if op == '-':
                return a - b
            if op == '/':
                return a / b
            if op == '*':
                return a * b
            if op == '**':
                return a ** b
            if op == '//':
                return a // b
        else:
            a = str(a)
            b = str(b)

        if op == '+':
            return a + b
        else:
            Etisdew.print('Warning:', 'You may not perform mathimatical operations in character form. Leave the "literal" variable on false.')

    @staticmethod
    def listexample(x, y):
        p = Etisdew.print
        p(' ',x)
        x.append(4)
        p(' ',x)
        x.extend(y)
        p(' ',x)
        x.pop(-3)
        p(' ',x)
        x.insert(-1, 99)
        p(' ',x)
        p(' ',len(x))
        p(' ',*[a * 1000 for a in x])

    @staticmethod
    def print_tuple(*args):
        for e in args:
            if type(e) is (int or str):
                Etisdew.print(' ',e)

    @staticmethod
    def sliceexample(a, s):
        p = Etisdew.print
        p(' ',a[1:2])
        p(' ',a[-2:-1])
        p(' ',a[-3:])
        p(' ',a[2:4])
        p(' ',a[1:])
        p(' ',a[:-1])
        p(' ',s[7:12])

    @staticmethod
    def compexample():
        p = Etisdew.print
        y = [x for x in range(0, 5)]
        p(' ', y)
        y = [x ** 3 for x in range(0, 10)]
        p(' ', y)
        a = ['foo', 'bar', 'baz']
        y = [x.upper() for x in a]
        p(' ', y)
        x = input('Enter comma-seperated numbers: ').split(',')
        y = [z for z in x]
        p(' ',y)

    def unpack(lat=0.0, lon=0.0, name='None'):
        Etisdew.print('{} {} {}'.format(lat, lon, name))
    @staticmethod
    def dictexample():
        waypoints = [
            {
                "lat": 44.052071,
                "lon": -123.086754,
                "name": "Eugene, Oregon"
            },
            {
                "lat": 37.774929,
                "lon": -122.419418,
                "name": "San Fransisco, California"
            },
            {
                "lat": 40.9135,
                "lon": -122.753086,
                "name": "Trinity Center, California"
            }
        ]
        waypoints.append({"lat": 0.0, "lon": 0.0, "name": "The Ocean"})

        for coord in waypoints:
            Etisdew.unpack(**coord)

    @staticmethod
    def funcexample():
        num = input("Enter a number: ")
        if int(num) % 2 == 0:
            return '    Even!'
        else:
            return '    Odd'

    @staticmethod
    def argsexample():
        p = Etisdew.print
        def f1(a, b):
            return a + b

        p(f1(1, 2))

        def f2(*args):
            closure = 0
            for item in args:
                closure += item
            return closure

        p(f2(1))                    # Should p 1
        p(f2(1, 3))                 # Should p 4
        p(f2(1, 4, -12))            # Should p -7
        p(f2(7, 9, 1, 3, 4, 9, 0))  # Should p 33

        a = [7, 6, 5, 4]

        # What thing do you have to add to make this work?
        p(f2(*a))    # Should p 22

        def f3(a, b=1):
            return a + b

        p(f3(1, 2))  # Should p 3
        p(f3(8))     # Should p 9

        def f4(**kwargs):
            for w in kwargs:
                p(f'{w}: {kwargs[w]}')

        f4(a=12, b=30)

        # Should print
        # key: city, value: Berkeley
        # key: population, value: 121240
        # key: founded, value: "March 23, 1868"
        f4(city="Berkeley", population=121240, founded="March 23, 1868")

        d = {
            "monster": "goblin",
            "hp": 3
        }

        # What thing do you have to add to make this work?
        f4(**d)

    @staticmethod
    def scopeexample():
        x = 12

        def changeX():
            nonlocal x
            x = 99

        changeX()

        # This prints 12. What do we have to modify in changeX() to get it to print 99?
        print(x)

        def outer():
            y = 120
            def inner():
                nonlocal y
                y = 999
            inner()
            print(y)
        outer()

    @staticmethod
    def fileioexample():
        f1 = open("foo.txt", "r")
        Etisdew.print(*f1.readlines())
        f1.close()

        f2 = open("foo_2.txt", "w")
        f2.write('This is text I wrote\nSecond Line\nThird Line\n')
        f2.close()

        f2 = open("foo_2.txt", "r")
        Etisdew.print(*f2.readlines())
        f2.close()

    @staticmethod
    def calexample():
        now = datetime.date.today()
        year, month, day = str(now).split('-')

        for item in sys.argv:
            if 'year' in item:
                year = item.split('=')[1]
            if 'month' in item:
                month = item.split('=')[1]

        Etisdew.print(calendar.month(int(year), int(month)))

    @staticmethod
    def classexample():
        class LatLon:
            def __init__(self, lat=0, lon=0, name=''):
                self.lat = lat
                self.lon = lon
                self.name = name

        class Waypoint(LatLon):
            def __init__(self, lat=0, lon=0, name=''):
                LatLon.__init__(self, lat=0, lon=0, name='')

        class Geocache(Waypoint):
            def __init__(self, lat=0, lon=0, name='', size=0, difficulty=0):
                Waypoint.__init__(self, lat=0, lon=0, name='')
                super().__init__(self)
                self.size = size
                self.difficulty = difficulty

        x = LatLon()
        y = Waypoint()
        z = Geocache()
        Etisdew.print(' ', z, y, x)

e = Etisdew()
