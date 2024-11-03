# A object can also be a function
class A():
    def __init__(self, a1):
        self.a = a1

    def __call__(self, b):
        return self.a + b
a = A(2)
print(a.a) # property access
print(a(3)) # object emulating a function


# A object can also be an iterator
class B():
    def __init__(self, a, b, c):
        self.items = [a,b,c]

    def __iter__(self):
        return (i for i in self.items)
b = B(2, 4, 5)
print(b.items) # property access
for i in b:
    print(i)


class Song(object):
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
    def __str__(self):
        return ('"%(title)s" by %(artist)s' %
                self.__dict__)
    @staticmethod
    def create_songs(songlist):
        for artist, title in songlist:
            yield Song(title, artist)
songs = (('Glen Hansard', 'Leave'),
         ('Stevie Ray Vaughan', 'Lenny'))
for song in Song.create_songs(songs):
    print(song)


# inheritance
class Math(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def execute(self):
        pass
class Sum(Math):
    def execute(self):
        return self.a + self.b
class Multi(Math):
    def execute(self):
        return self.a * self.b
for m in[Sum(2,3), Multi(2,3)]:
    print(m.execute())


# calling supper and abstract methods (need to use module abc, interesting looks like a hack)
from abc import ABC, abstractmethod
class Instrument(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def has_strings(self):
        pass
class PercussionInstrument(Instrument):
    def has_strings(self):
        return False
class StringInstrument(Instrument):
    def __init__(self, name, count):
        super(StringInstrument, self).__init__(name)
        self.count = count
    def has_strings(self):
        return True
class Guitar(StringInstrument):
    def __init__(self):
        super(Guitar, self).__init__('guitar', 6)
for instrument in [Guitar(), PercussionInstrument("drum"), StringInstrument("violin", 4)]:
    num_strings = f" # of string: {instrument.count}" if instrument.has_strings() else ""
    print(f"The {instrument.name} has strings: {instrument.has_strings()}.{num_strings}")


# Multiple Inheritance
class Analyzable(object):
    def __init__(self, a):
        self.name = a
    def analyze(self):
        print(f'I am a {self.__class__.__name__} {self.name}')
class Flute(Instrument, Analyzable):
    def has_strings(self):
        return False
flute = Flute('sweet')
flute.analyze()


#defining a method as a property
class Course(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.enrolled = 0
    def enroll(self):
        self.enrolled += 1
    @property
    def open(self):
        return self.capacity - self.enrolled

course = Course(12)
course.enroll()
course.enroll()
print (course.open) # instead of course.open()


# making sure you execute something when setting speed
class Car(object):
    def __init__(self, name, maxspeed):
        self.name = name
        self.maxspeed = maxspeed
        self.__speed = 0
    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self, value):
        s = int(value)
        s = max(0, s)
        self.__speed = min(self.maxspeed, s)
car = Car('Lada', 32)
car.speed = 100
print('My {name} is going {speed} mph!'.format(name=car.name, speed=car.speed))
car.speed = 24
print('My {name} is going {speed} mph!'.format(name=car.name, speed=car.speed))