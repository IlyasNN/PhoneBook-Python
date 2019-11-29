from Other import cls
from datetime import datetime, date, timedelta
from Person import Person


def currentAge(phoneBook):
    cls()
    print(
        '\tTo find information about age of person from phoneBook enter name and surname in format(Name Surname) \n\t\tOr '
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
                agePerson = phoneBook[searchKey]

                if agePerson.birthday is not None:
                    now = datetime.now().date()
                    delta = now - agePerson.birthday
                    print(
                        '\tNow ' + agePerson.name + ' ' + agePerson.surname + ' is ' + str(
                            int(delta.days / 365)) + ' years old\n')
                else:
                    print("\tThere is no information about the date of birthday\n\n")

            else:
                print('\tThere is no person with such name and surname\n')

        except BaseException:
            print('\n\tWrong name and surname format\n\n')

    else:
        cls()
