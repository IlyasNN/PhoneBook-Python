from Person import Person
from datetime import datetime


def cls(): print("\n" * 100)


# Function that parse a string with the information about a person a creates a Person object
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


def menu1():
    cls()
    print(' WHOLE PHONEBOOK\n')
    i = 0
    for person in phoneBook.values():
        i += 1
        print('  ', i)
        print('Name    : ' + person.name)
        print('Surname : ' + person.surname)
        print('Phones  :')
        for key in person.phones:
            if (person.phones[key] != None):
                print(' ' + key + ': ' + person.phones[key])
        if person.birthday != None:
            print('Birthday: ' + person.birthday.strftime('%d.%m.%Y'))
        print()
    print('Total number of contacts: ', len(phoneBook))
    print('\n-----------------------------\n')


def menu2():
    pass


def menu3():
    cls()
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


if __name__ == "__main__":

    phoneBook = {}
    with open('DataBase.txt', 'r') as readFile:
        for line in readFile:
            line = line.replace('\n', '')
            newOne = parse(line)
            phoneBook[newOne.name + ' ' + newOne.surname] = newOne

    print(
        'Hello - instruction\n1.show\n2.search\n3.add new person\n4.delete some person\n5.change information about a person\n6.age of a person\nquit\n')
    menu = input('Enter: ')
    while menu != 'quit':
        menu = int(menu)
        if menu == 1:
            menu1()
        elif menu == 2:
            menu2()
        elif menu == 3:
            menu3()
        elif menu == 4:
            menu4()
        elif menu == 5:
            menu5()
        elif menu == 6:
            menu6()
        # wrong command
        print(
            '1.show\n2.search\n3.add new person\n4.delete some person\n5.change information about a person\n6.age of a person\nquit\n')
        menu = input('Enter: ')

    with open('DataBase.txt', 'w') as writeFile:
        for key in phoneBook:
            writeFile.write(phoneBook[key].to_str() + '\n')
