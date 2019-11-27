import Main
from datetime import datetime, date
from Person import Person


def change(phoneBook):
    Main.cls()
    print('To change information about a person from phone book enter name and surname in format(Name Surname) or '
          'enter \'quit\' to quit')
    menu = input('Enter: ')
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
                print('Contact was found:\n')
                phoneBook[searchKey].print()
                changePerson = phoneBook[searchKey]
                print(
                    'Choose a field to change:\n1.name\n2.surname\n3.mobile number\n4.home number\n5.work '
                    'number\n6.date of birhday\n\'quit\' to quit')
                menu2 = input('Enter: ')
                while menu2 != 'quit':
                    try:
                        menu2 = int(menu2)
                    except BaseException:
                        menu2 = 7

                    if menu2 == 1:
                        try:
                            name = input('Enter new name: ')
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
                            surname = input('Enter new surname: ')
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
                            phone = input('Enter new mobile number in format (8XXXXXXXXXX) or \'del\' to delete: ')
                            phone = phone.replace(' ', '').replace('+7', '8')
                            if phone == 'del':
                                phoneBook[searchKey].phones['mobile'] = None
                            else:
                                if not phone.isdigit():
                                    raise Exception()
                                phoneBook[searchKey].phones['mobile'] = phone
                        except BaseException:
                            print('Wrong phone number format, try one more time\n')

                    elif menu2 == 4:
                        try:
                            phone = input('Enter new home number in format (8XXXXXXXXXX) or \'del\' to delete: ')
                            phone = phone.replace(' ', '').replace('+7', '8')
                            if phone == 'del':
                                phoneBook[searchKey].phones['home'] = None
                            else:
                                if not phone.isdigit():
                                    raise Exception()
                                phoneBook[searchKey].phones['home'] = phone
                        except BaseException:
                            print('Wrong phone number format, try one more time\n')
                    elif menu2 == 5:
                        try:
                            phone = input('Enter new work number in format (8XXXXXXXXXX) or \'del\' to delete: ')
                            phone = phone.replace(' ', '').replace('+7', '8')
                            if phone == 'del':
                                phoneBook[searchKey].phones['work'] = None
                            else:
                                if not phone.isdigit():
                                    raise Exception()
                                phoneBook[searchKey].phones['work'] = phone
                        except BaseException:
                            print('Wrong phone number format, try one more time\n')
                    elif menu2 == 6:
                        try:
                            newDate = input('Enter new date of birthday in format (dd.mm.yyyy) or \'del\' to delete: ')
                            if newDate == 'del':
                                phoneBook[searchKey].birthday = None
                            else:
                                newDate = newDate.replace(' ', '')
                                newDate = newDate.replace('/', '.').replace('-', '.')
                                phoneBook[searchKey].birthday = datetime.strptime(newDate, '%d.%m.%Y').date()

                        except BaseException:
                            print('Wrong date format, try one more time\n')

                    print('\n\n\nChanges were saved:\n')
                    phoneBook[searchKey].print()

                    print(
                        '\n\nChoose one more field to change:\n1.name\n2.surname\n3.mobile number\n4.home '
                        'number\n5.work number\n6.date of birhday\n\'quit\' to quit')
                    menu2 = input('Enter: ')

                Main.cls()
            else:
                print('There is no person with such name and surname')

        except BaseException:
            print('Wrong name and surname format')
    else:
        Main.cls()
