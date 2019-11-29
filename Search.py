from datetime import datetime

from Other import cls
from Show import showSearch


def search(phoneBook):
    cls()
    searchBook = phoneBook.copy()
    print('\tTo find a person in phone book choose a field for search:')
    print('\t(You can search till the command quit narrowing down you search)')
    print('\t\t1.name\n\t\t2.surname\n\t\t3.name and surname\n\t\t4.phone\n\t\t5.date of birthday\n\t\t\'quit\' to quit\n')
    menu = input('Enter: ')
    while menu != 'quit':
        try:
            menu = int(menu)
        except BaseException:
            menu = 6
        if menu == 1:
            try:
                name = input('\tEnter a name:')
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
                surname = input('\tEnter a surname:')
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
                nameSurname = input('\tEnter name and surname in format (Name Surname):')
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
                phone = input('\tEnter phone number:')
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
                birthday = input('\tEnter date of birthday in format (dd.mm):')
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
            '\tChoose a field for search:\n\t\t1.name\n\t\t2.surname\n\t\t3.name and surname\n\t\t4.phone\n\t\t5.date of birthday\n\t\t\'quit\' to quit\n')
        menu = input('\tEnter: ')

        cls()
