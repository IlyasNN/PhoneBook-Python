from Add import parse, add
from Delete import delete
from Search import search
from Show import show


def cls(): print("\n" * 100)


# Function that parse a string with the information about a person a creates a Person object


def menu2():
    pass


def main():
    phoneBook = {}
    with open('DataBase.txt', 'r') as readFile:
        for line in readFile:
            line = line.replace('\n', '')
            newOne = parse(line)
            phoneBook[newOne.name + ' ' + newOne.surname] = newOne

    print(
        'Hello - instruction\nChoose what to do with your phonebook: \n1.show\n2.search\n3.add new person\n4.delete some person\n5.change information about a person\n6.age of a person\nquit\n')
    menu = input('Enter: ')
    while menu != 'quit':
        try:
            menu = int(menu)
        except BaseException:
            menu = 7
        if menu == 1:
            show(phoneBook)
        elif menu == 2:
            search(phoneBook)
        elif menu == 3:
            add(phoneBook)
        elif menu == 4:
            delete(phoneBook)
        elif menu == 5:
            menu5()
        elif menu == 6:
            menu6()
        # wrong command
        print(
            'Choose what to do with your phonebook: \n1.show\n2.search\n3.add new person\n4.delete some person\n5.change information about a person\n6.age of a person\nquit\n')
        menu = input('Enter: ')

    with open('DataBase.txt', 'w') as writeFile:
        for key in phoneBook:
            writeFile.write(phoneBook[key].to_str() + '\n')


main()