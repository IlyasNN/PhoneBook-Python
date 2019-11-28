import Main


def delete(phoneBook):
    Main.cls()
    print('To delete a person from phoneBook choose a field for deletion search:')
    print('1.name and surname\n2.name\n3.surname\n4.phone\nquit\n')
    menu = input('Enter: ')
    if menu != 'quit':
        try:
            menu = int(menu)
        except BaseException:
            menu = 6

        listDelete = []

        if menu == 1:
            try:
                nameSurname = input('Enter name and surname in format (Name Surname):')
                ns = nameSurname.split(' ')
                ns[0] = ns[0].title()
                ns[1] = ns[1].title()
                for key in list(phoneBook):
                    if phoneBook[key].name == ns[0] and phoneBook[key].surname == ns[1]:
                        listDelete.append(key)
            except BaseException:
                print('wrong name or surname format, try one more time\n')

        elif menu == 2:
            try:
                name = input('Enter a name:')
                name = name.replace(' ', '')
                name = name.title()
                for key in list(phoneBook):
                    if phoneBook[key].name == name:
                        listDelete.append(key)
            except BaseException:
                print('Wrong name format, try one more time\n')

        elif menu == 3:
            try:
                surname = input('Enter a surname:')
                surname = surname.replace(' ', '')
                surname = surname.title()
                for key in list(phoneBook):
                    if phoneBook[key].surname == surname:
                        listDelete.append(key)
            except BaseException:
                print('Wrong surname format, try one more time\n')

        elif menu == 4:
            try:
                phone = input('Enter phone number in:')
                phone = phone.replace(' ', '').replace('+7', '8')
                if not phone.isdigit():
                    raise Exception()
                for key in list(phoneBook):
                    if phoneBook[key].phones['mobile'] == phone or phoneBook[key].phones['home'] == phone or \
                            phoneBook[key].phones['work'] == phone:
                        listDelete.append(key)

            except BaseException:
                print('wrong phone format, try one more time\n')

        print('List of contacts for deletion:\n')
        for element in listDelete:
            phoneBook[element].print()

        print('\nDo you want to delete all of them? Choose:\n1.Yes\n2.Cancel\n')
        menu2 = input('Enter: ')
        try:
            menu2 = int(menu2)
        except BaseException:
            menu2 = 2
        if menu2 == 1:
            for key in listDelete:
                del phoneBook[key]

    Main.cls()
