import datetime


class Person(object):

    def __init__(self):
        self.name = ''
        self.surname = ''
        self.phones = {'mobile': None, 'home': None, 'work': None}
        self.birthday = datetime.date
        pass

    def to_str(self):
        string = self.name + ';'
        string = string + self.surname + ';'
        if self.phones['mobile']:
            string = string + 'mobile:' + self.phones['mobile']
            if self.phones['home']:
                string = string + ','
        if self.phones['home']:
            string = string + 'home:' + self.phones['home']
            if self.phones['work']:
                string = string + ','
        if self.phones['work']:
            string = string + 'work:' + self.phones['work']

        if self.birthday:
            string = string + ';' + self.birthday.strftime('%d.%m.%Y')
        return string
