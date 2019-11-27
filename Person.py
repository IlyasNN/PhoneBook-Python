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

    def print(self):

        print('Name    : ' + self.name)
        print('Surname : ' + self.surname)
        print('Phones  :')
        for key in self.phones:
            if (self.phones[key] != None):
                print(' ' + key + ': ' + self.phones[key])
        if self.birthday != None:
            print('Birthday: ' + self.birthday.strftime('%d.%m.%Y'))
        print()
# Создаём таблицу относительных частот
