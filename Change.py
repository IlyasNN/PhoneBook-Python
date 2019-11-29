from Other import cls
from datetime import datetime, date
from Person import Person


def change(phoneBook):
    cls()
    print(
        '\tTo change information about a person from phoneBook enter name and surname in format(Name Surname) \n\t\tOr '
        'enter \'quit\' to quit')
    menu = input('\n\tEnter: ')
    if menu != 'quit':
        try:
            nameSurname = menu
            ns = nameSurname.split(' ')
            searchKey = None
            ns[0] = ns[0].title()
            ns[1] = ns[1].title()
            for key in list(phoneBook):
                if phoneBook[key].name == ns[0] and phoneBook[key].surname == ns[1]:
                    searchKey = key

            if searchKey is not None:
                print('\n\tContact was found:\n')
                phoneBook[searchKey].print()
                changePerson = phoneBook[searchKey]
                print(
                    '\n\tChoose a field to change:\n\t\t1.name\n\t\t2.surname\n\t\t3.mobile number\n\t\t4.home number\n\t\t5.work '
                    'number\n\t\t6.date of birhday\n\t\t\'quit\' to quit')
                menu2 = input('\n\tEnter: ')
                while menu2 != 'quit':
                    try:
                        menu2 = int(menu2)
                    except BaseException:
                        menu2 = 7

                    if menu2 == 1:
                        try:
                            name = input('\tEnter new name: ')
                            name = name.replace(' ', '')
                            name = name.title()
                            if (name + ' ' + changePerson.surname) in phoneBook:
                                print(
                                    'There is such contact  ' + name + ' ' + changePerson.surname + ' in phoneBook, try one more time')
                            else:
                                phoneBook[name + ' ' + changePerson.surname] = phoneBook.pop(searchKey)
                                phoneBook[name + ' ' + changePerson.surname].name = name
                                searchKey = name + ' ' + changePerson.surname
                        except BaseException:
                            print('Wrong name format, try one more time\n')


                    elif menu2 == 2:
                        try:
                            surname = input('\tEnter new surname: ')
                            surname = surname.replace(' ', '')
                            surname = surname.title()
                            if (changePerson.name + ' ' + surname) in phoneBook:
                                print(
                                    'There is such contact  ' + changePerson.name + ' ' + surname + ' in phoneBook, try one more time')
                            else:
                                phoneBook[changePerson.name + ' ' + surname] = phoneBook.pop(searchKey)
                                phoneBook[changePerson.name + ' ' + surname].surname = surname
                                searchKey = changePerson.name + ' ' + surname
                        except BaseException:
                            print('Wrong surname format, try one more time\n')
                    elif menu2 == 3:
                        try:
                            phone = input('\tEnter new mobile number or \'del\' to delete: ')
                            phone = phone.replace(' ', '').replace('+7', '8')
                            if phone == 'del':
                                if (phoneBook[searchKey].phones['home'] is None and phoneBook[searchKey].phones['work'] is None):
                                    raise Exception()
                                phoneBook[searchKey].phones['mobile'] = None
                            else:
                                if not phone.isdigit():
                                    raise Exception()
                                phoneBook[searchKey].phones['mobile'] = phone
                        except BaseException:
                            print(
                                '\nWrong phone number format or you try to delete only (last) number, try one more time\n')

                    elif menu2 == 4:
                        try:
                            phone = input('\tEnter new home number \'del\' to delete: ')
                            phone = phone.replace(' ', '').replace('+7', '8')
                            if phone == 'del':
                                if (phoneBook[searchKey].phones['mobile'] is None and phoneBook[searchKey].phones['work'] is None):
                                    raise Exception()
                                phoneBook[searchKey].phones['home'] = None
                            else:
                                if not phone.isdigit():
                                    raise Exception()
                                phoneBook[searchKey].phones['home'] = phone
                        except BaseException:
                            print(
                                '\nWrong phone number format or you try to delete only (last) number, try one more time\n')
                    elif menu2 == 5:
                        try:
                            phone = input('\tEnter new work number or \'del\' to delete: ')
                            phone = phone.replace(' ', '').replace('+7', '8')
                            if phone == 'del':
                                if (phoneBook[searchKey].phones['mobile'] is None and phoneBook[searchKey].phones['home'] is None):
                                    raise Exception()
                                phoneBook[searchKey].phones['work'] = None
                            else:
                                if not phone.isdigit():
                                    raise Exception()
                                phoneBook[searchKey].phones['work'] = phone
                        except BaseException:
                            print(
                                '\nWrong phone number format or you try to delete only (last) number, try one more time\n')
                    elif menu2 == 6:
                        try:
                            newDate = input(
                                '\tEnter new date of birthday in format (dd.mm.yyyy) or \'del\' to delete: ')
                            if newDate == 'del':
                                phoneBook[searchKey].birthday = None
                            else:
                                newDate = newDate.replace(' ', '')
                                newDate = newDate.replace('/', '.').replace('-', '.')
                                phoneBook[searchKey].birthday = datetime.strptime(newDate, '%d.%m.%Y').date()

                        except BaseException:
                            print('Wrong date format, try one more time\n')

                    print('\nChanges were saved:\n')
                    phoneBook[searchKey].print()

                    print(
                        '\n\n\tChoose one more field to change:\n\t\t1.name\n\t\t2.surname\n\t\t3.mobile number\n\t\t4.home number\n\t\t5.work '
                        'number\n\t\t6.date of birhday\n\t\t\'quit\' to quit')
                    menu2 = input('\n\tEnter: ')

                cls()
            else:
                print('\t\tThere is no person with such name and surname\n\n')

        except BaseException:
            print('Wrong name and surname format')
    else:
        cls()
