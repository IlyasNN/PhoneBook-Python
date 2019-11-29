from Other import cls


def delete(phoneBook):
    cls()
    print('\tTo delete a person from phoneBook choose a field for deletion search:')
    print('\t\t1.name and surname\n\t\t2.name\n\t\t3.surname\n\t\t4.phone\n\t\t\'quit\' to quit\n')
    menu = input('\tEnter: ')
    if menu != 'quit':
        try:
            menu = int(menu)
        except BaseException:
            menu = 6

        listDelete = []

        if menu == 1:
            try:
                nameSurname = input('\n\tEnter name and surname in format (Name Surname):')
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
                name = input('\n\tEnter a name:')
                name = name.replace(' ', '')
                name = name.title()
                for key in list(phoneBook):
                    if phoneBook[key].name == name:
                        listDelete.append(key)
            except BaseException:
                print('Wrong name format, try one more time\n')

        elif menu == 3:
            try:
                surname = input('\n\tEnter a surname:')
                surname = surname.replace(' ', '')
                surname = surname.title()
                for key in list(phoneBook):
                    if phoneBook[key].surname == surname:
                        listDelete.append(key)
            except BaseException:
                print('Wrong surname format, try one more time\n')

        elif menu == 4:
            try:
                phone = input('\n\tEnter phone number:')
                phone = phone.replace(' ', '').replace('+7', '8')
                if not phone.isdigit():
                    raise Exception()
                for key in list(phoneBook):
                    if phoneBook[key].phones['mobile'] == phone or phoneBook[key].phones['home'] == phone or \
                            phoneBook[key].phones['work'] == phone:
                        listDelete.append(key)

            except BaseException:
                print('wrong phone format, try one more time\n')

        print('\tList of contacts for deletion:\n')
        for element in listDelete:
            phoneBook[element].print()

        print('\n\t\tDo you want to delete all of them? Choose:\n\t1.Yes\n\t2.Cancel\n')
        menu2 = input('Enter: ')
        try:
            menu2 = int(menu2)
        except BaseException:
            menu2 = 2
        if menu2 == 1:
            for key in listDelete:
                del phoneBook[key]

    cls()
