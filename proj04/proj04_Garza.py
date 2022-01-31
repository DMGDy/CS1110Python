#!/usr/bin/python

#Project No.: 04
#Author: Dylan-Matthew Garza
#Description: This program reads a masterfile containing a bank account numbers, balances and names in a line in that respective order. The program prompts the user to access to read the file with inputting the file prefix then if successful is prompted to input one of 4 commands that do action on the bank account. Once the user is done modifying the accounts, a new file is written with all modifications made.
def main():
    end = 999999    #declaring variables that will be later used in the program.
    num = 0
    inp = str(input("Enter a file prefix: "))
    try:
        f = open(f'{inp}_old.txt','r')
    except IOError:     #if an invalid file prefix, whole program is exited.
        print(f'\n The file name {inp}_old.txt does not exist')
        exit()
    else:
        f.close()
    with open(f'{inp}_old.txt','r') as f0, open(f'{inp}_new.txt','w') as f1:    #opens files in a loop so that no line is necessary for closing files
        while num != end:
            line = f0.readline()
            num = round(get_number(line),2)
            if num == 999999:       #lines are read until the last line of the file where 999999 is read.
                print(f'There are no more entries')
                f1.write(f'{end}')
                exit()
            bal = get_balance(line)
            nam = get_name(line)
            print(f'Verifying Input: {num} {bal} {nam}')    #prints begining of each loop
            inpt = None
            while inpt != 'a':      #an input of a will end the while loop after executing if statement of a
                try:
                    inpt = input('\033[AEnter a command (a,c,d,w): ')
                    if inpt != 'a'and inpt != 'c' and inpt != 'd' and inpt != 'w':
                        print(f'Not a valid input.')
                    if inpt == 'c' and bal == 0:
                        print(f'Account is closed')
                        closed = True
                        break
                    if inpt == 'c' and bal != 0:
                        print(f'Account not closed because money is still in it\n')
                        closed = False
                    if inpt == 'w' and bal != 0:
                        inpt = None
                        wtdr = float(input('Enter withdrawal amount: '))
                        while wtdr > bal:
                            wtdr = float(input('Cannot withdraw more than balance.\nEnter withdrawal amount: '))
                        bal = float("{:.2f}".format(bal - wtdr))    #formats ballance to round to 2 decimals.
                        print(f'New balance: {num} {bal} {nam}')
                    if inpt == 'w' and bal == 0:
                        print(f'No money left in balance')
                    if inpt == 'd':
                        dep = float(input('Enter deposit amount: '))
                        bal = float('{:2f}'.format(bal + dep))
                        if bal > 9999999.99:    #maximum balance is given as 9999999.99 so any balance above is rounded down to the program maximum.
                            bal = 9999999.99
                        print(f'New balance: {num} {bal} {nam}')
                    if inpt == 'a':
                        bal = "{:>10}".format(bal)      #formats balance such that it is 10 characters long with spaces taking up non float values.
                        f1.write(f'{num} {bal} {nam}')
                except ValueError:      #any input error results in a Value Error so program will reprompt for a command.
                    print('Invalid input, try again')
                    continue

    return 0
#following functions are called to extract the sections of the line containing data

def get_number(line):
    acc_number = int(line[0:6])
    return acc_number


def get_balance(line):
    acc_balance = float(line[7:17])
    return acc_balance


def get_name(line):
    acc_name = str(line[18:])
    return acc_name


main()
