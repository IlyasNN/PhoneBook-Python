from datetime import datetime
from Person import Person
import Main


def parse(string):
    newPerson = Person()
    string = string.replace(' ', '')
    blocks = string.split(';')

    # Checks a block with name and surname
    try:
        name = blocks[0]
        name = name.title()
        newPerson.name = name

        surname = blocks[1]
        surname = surname.title()
        newPerson.surname = surname
    except BaseException:
        print("Wrong name or surname format\nCheck the format please and reenter it")
        return None

    # Checks a block with the date of birthday (if it exists)

    # Checks a block with phones (a few phone numbers are available)
    try:
        phones = blocks[2].split(',')
        for phone in phones:
            phoneParts = phone.split(':')
            phoneParts[0] = phoneParts[0].lower()
            phoneParts[1] = phoneParts[1].replace('+7', '8')
            if phoneParts[0] in newPerson.phones:
                newPerson.phones[phoneParts[0]] = phoneParts[1]
            else:
                raise Exception('No such key')
    except BaseException:
        print("Wrong phones format\nCheck the format please and reenter it")
        return None

    if len(blocks) >= 4:
        try:
            blocks[3] = blocks[3].replace('/', '.').replace('-', '.')
            newPerson.birthday = datetime.strptime(blocks[3], '%d.%m.%Y').date()
        except BaseException:
            print("Wrong date format\nCheck the format please and reenter it")
            return None
    else:
        newPerson.birthday = None

    return newPerson


def add(phoneBook):
    Main.cls()
    print('To add new person in phone book enter information in the following format:')
    print('Name;Surname;mobile:8xxxxxxxx,home:xxxxxxx,work:xxxxxxxx;dd.mm.yyyy')
    print('If some fields are missing, just dont enter it')
    string = input('Enter: ')
    newOne = parse(string)
    # Enter a string with the information until it has a right format
    while newOne == None:
        string = input('Enter: ')
        newOne = parse(string)

    # Check if there is a person with such Name and Surname
    f = (newOne.name + ' ' + newOne.surname) in phoneBook
    if not f:
        phoneBook[newOne.name + ' ' + newOne.surname] = newOne

    #
    while f:
        print('There is a contact with such Name and Surname\nChoose what to do:')
        print('1.replace\n2.reenter information\n3.quit')
        menu = int(input('Enter: '))
        # Replace the information
        if menu == 1:
            del (phoneBook[newOne.name + ' ' + newOne.surname])
            phoneBook[newOne.name + ' ' + newOne.surname] = newOne
            f = False
        # Reenter a string
        elif menu == 2:
            print('To add new person in phone book enter information in the following format:')
            print('Name;Surname;mobile:8xxxxxxxx,home:xxxxxxx,work:xxxxxxxx;dd.mm.yyyy')
            print('If some fields are missing, just dont enter it')
            while newOne == None:
                string = input('Enter: ')
                newOne = parse(string)
            f = (newOne.name + ' ' + newOne.surname) in phoneBook
            if not f:
                phoneBook[newOne.name + ' ' + newOne.surname] = newOne
        # quit
        elif menu == 3:
            f = False
        # wrong command
        else:
            print('WRONG COMMAND')
            f = True
