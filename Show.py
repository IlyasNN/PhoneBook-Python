from Other import cls


def show(phoneBook):
    cls()
    print(' WHOLE PHONEBOOK:\n')
    i = 0
    for person in phoneBook.values():
        person.print()
    print('Total number of contacts: ', len(phoneBook))
    print('\n-----------------------------\n')


def showSearch(searchBook):
    cls()
    print(' PHONEBOOK AFTER CURRENT SEARCH:\n')
    i = 0
    for person in searchBook.values():
        i += 1
        print('\t  ', i)
        print('\tName    : ' + person.name)
        print('\tSurname : ' + person.surname)
        print('\tPhones  :')
        for key in person.phones:
            if (person.phones[key] != None):
                print('\t  ' + key + ': ' + person.phones[key])
        if person.birthday != None:
            print('\tBirthday: ' + person.birthday.strftime('%d.%m.%Y'))
        print()
    print('Number of contacts that were found: ', len(searchBook))
    print('\n-----------------------------\n')


def showBirthday(searchBook):
    cls()
    print('\tLIST OF CONTACTS WHO WILL CELEBRATE BIRTHDAY SOON:\n')
    i = 0
    for person in searchBook.values():
        i += 1
        person.print()
    print('\t\tNumber of contacts that were found: ', len(searchBook))
    print('\n\t-----------------------------\n')
