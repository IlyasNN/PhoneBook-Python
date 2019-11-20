import datetime


class Person(object):

    def __init__(self):
        self.name = ''
        self.surname = ''
        self.phones = {'mobile': None, 'home': None, 'work': None}
        self.birthday = datetime.date
        pass
