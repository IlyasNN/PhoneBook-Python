import Main


def show(phoneBook):
    Main.cls()
    print(' WHOLE PHONEBOOK\n')
    i = 0
    for person in phoneBook.values():
        person.print()
    print('Total number of contacts: ', len(phoneBook))
    print('\n-----------------------------\n')


def showSearch(searchBook):
    Main.cls()
    print(' PHONEBOOK AFTER CURRENT SEARCH\n')
    i = 0
    for person in searchBook.values():
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
    print('Number of contacts that were found: ', len(searchBook))
    print('\n-----------------------------\n')
