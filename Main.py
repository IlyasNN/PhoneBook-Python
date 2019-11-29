from Add import add, parse
from Delete import delete
from Search import search
from Show import show
from Change import change
from CurrentAge import currentAge
from BirthdayList import birthdayList





# Function that parse a string with the information about a person a creates a Person object


def main():
    # dictionary with keys(Name Surname) and objects of Person class
    phoneBook = {}
    # reading database
    with open('DataBase.txt', 'r') as readFile:
        for line in readFile:
            line = line.replace('\n', '')
            newOne = parse(line)
            phoneBook[newOne.name + ' ' + newOne.surname] = newOne

    #menu
    print('\n\n\nHELLO! THIS IS THE BEST PHONEBOOK FROM THE BEST PROGRAMMER OF THE WORLD!')
    print('\t\tIT\'S WITH LOVE \n\t\t\tBY ILYA SOLOVOV')
    print('\nChoose what to do with your phonebook: \n\t1.show\n\t2.search\n\t3.add new person\n\t4.delete some people\n\t5.change information about a person\n\t6.find out the age of a person\n\t7.get list of contacts who will celebrate Birhday soon\n\t\'quit\' to quit\n')
    menu = input('Enter: ')
    while menu != 'quit':
        try:
            menu = int(menu)
        except BaseException:
            menu = 8
        if menu == 1:
            show(phoneBook)
        elif menu == 2:
            search(phoneBook)
        elif menu == 3:
            add(phoneBook)
        elif menu == 4:
            delete(phoneBook)
        elif menu == 5:
            change(phoneBook)
        elif menu == 6:
            currentAge(phoneBook)
        elif menu == 7:
            birthdayList(phoneBook)
        else:
            print('\tWrong command, try one more time :-)\n')
        print(
            'Choose what to do with your phonebook: \n\t1.show\n\t2.search\n\t3.add new person\n\t4.delete some person\n\t5.change information about a person\n\t6.age of a person\n\t7.get list of contacts who will celebrate Birhday soon\n\t\'quit\' to quit\n')
        menu = input('Enter: ')

    # rewriting database
    with open('DataBase.txt', 'w') as writeFile:
        for key in phoneBook:
            writeFile.write(phoneBook[key].to_str() + '\n')


main()
