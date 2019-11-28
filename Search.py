from datetime import datetime

import Main
from Show import showSearch


def search(phoneBook):
    Main.cls()
    searchBook = phoneBook.copy()
    print('To find a person in phone book choose a field for search:')
    print('(You can search till the command quit narrowing down you search)')
    print('1.name\n2.surname\n3.name and surname\n4.phone\n5.date of birthday\nquit\n')
    menu = input('Enter: ')
    while menu != 'quit':
        try:
            menu = int(menu)
        except BaseException:
            menu = 6
        if menu == 1:
            try:
                name = input('Enter a name:')
                name = name.replace(' ', '')
                name = name.title()
                for key in list(searchBook):
                    if searchBook[key].name != name:
                        del searchBook[key]
                showSearch(searchBook)
            except BaseException:
                print('Wrong name format, try one more time\n')

        elif menu == 2:
            try:
                surname = input('Enter a surname:')
                surname = surname.replace(' ', '')
                surname = surname.title()
                for key in list(searchBook):
                    if searchBook[key].surname != surname:
                        del searchBook[key]
                showSearch(searchBook)
            except BaseException:
                print('Wrong surname format, try one more time\n')

        elif menu == 3:
            try:
                nameSurname = input('Enter name and surname in format (Name Surname):')
                ns = nameSurname.split(' ')
                ns[0] = ns[0].title()
                ns[1] = ns[1].title()
                for key in list(searchBook):
                    if searchBook[key].name != ns[0] and searchBook[key].surname != ns[1]:
                        del searchBook[key]
                showSearch(searchBook)
            except BaseException:
                print('wrong name or surname format, try one more time\n')

        elif menu == 4:
            try:
                phone = input('Enter phone number in format(8XXXXXXXX):')
                phone = phone.replace(' ', '').replace('+7', '8')
                for key in list(searchBook):
                    if searchBook[key].phones['mobile'] != phone and searchBook[key].phones['home'] != phone and \
                            searchBook[key].phones['work'] != phone:
                        del searchBook[key]
                showSearch(searchBook)
            except BaseException:
                print('wrong phone format, try one more time\n')

        elif menu == 5:
            try:
                birthday = input('Enter date of birthday in format (dd.mm):')
                birthday = birthday.replace(' ', '')
                DM = birthday.split('.')
                day = DM[0]
                month = DM[1]
                for key in list(searchBook):
                    if searchBook[key].birthday is None or not (searchBook[key].birthday.day == int(day) and
                                                                searchBook[key].birthday.month == int(month)):
                        del searchBook[key]
                showSearch(searchBook)
            except BaseException:
                print('wrong date format, try one more time\n')

        # wrong command
        print(
            'Choose a field for search:\n1.name\n2.surname\n3.name and surname\n4.date of birthday\nquit\n')
        menu = input('Enter: ')

        Main.cls()
