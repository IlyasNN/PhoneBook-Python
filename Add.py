from datetime import datetime
from Person import Person
from Other import cls


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
            if not (phoneParts[1].isdigit() and len(phoneParts[1]) <= 11):
                raise Exception()
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
    cls()
    print('\tTo add new person in phone book enter information in the following format:')
    print('\t\tName;Surname;mobile:8xxxxxxxx,home:xxxxxxx,work:xxxxxxxx;dd.mm.yyyy')
    print('\tIf some fields are missing, just dont enter it (at least one phone number is needed)')
    print('\t\texample: Ivan; Ivanov; mobile:88005553535, home:2523772; 01.01.2000')
    print('\t\texample: Andrey; Andreev; mobile:88005553535')
    print('\t\tOr enter \'quit\' to quit')
    string = input('\n\tEnter: ')
    string = string.replace(' ', '')
    if string != 'quit':
        newOne = parse(string)
        # Enter a string with the information until it has a right format
        while newOne == None:
            string = input('Enter: ')
            newOne = parse(string)

        # Check if there is a person with such Name and Surname
        f = (newOne.name + ' ' + newOne.surname) in phoneBook
        if not f:
            phoneBook[newOne.name + ' ' + newOne.surname] = newOne

        newOne = None
        #
        while f:
            print('\n\tThere is a contact with such Name and Surname or wrong command\n\tChoose what to do:\n')
            print('\t\t1.replace\n\t\t2.reenter information\n\t\t3.quit')
            try:
                menu = int(input('\n\tEnter: '))
            except BaseException:
                menu = 4
            # Replace the information
            if menu == 1:
                del (phoneBook[newOne.name + ' ' + newOne.surname])
                phoneBook[newOne.name + ' ' + newOne.surname] = newOne
                f = False
            # Reenter a string
            elif menu == 2:
                print('\tTo add new person in phone book enter information in the following format:')
                print('\t\tName;Surname;mobile:8xxxxxxxx,home:xxxxxxx,work:xxxxxxxx;dd.mm.yyyy')
                print('\tIf some fields are missing, just dont enter it (at least one phone number is needed)')
                print('\t\texample: Ivan; Ivanov; mobile:88005553535, home:2523772; 01.01.2000')
                print('\t\texample: Andrey; Andreev; mobile:88005553535')
                while newOne == None:
                    string = input('\n\tEnter: ')
                    newOne = parse(string)
                f = (newOne.name + ' ' + newOne.surname) in phoneBook
                if not f:
                    phoneBook[newOne.name + ' ' + newOne.surname] = newOne
                else:
                    newOne = None
            # quit
            elif menu == 3:
                f = False
            # wrong command
            else:
                print('\n\t\tWRONG COMMAND')
                f = True
    cls()
