#!/usr/bin/python

#Project No.: 03
#Author: Dylan-Matthew Garza
#Description: This program reads an integer input from the user then prompts the user to input the integer amount of string to which the program will count the frequency of each letter and display an asterisk for each instance.

import testModule

def main(): #gets input from user for how many strings to enter and calls other functions
    empl = [0]*26 
    char = None
    char = list(map(chr, range(97,123))) 
    m = None
    while True: 
        try:
            print("Enter the number of strings you would like to read: ")
            m = int(input())
            if m <= 0:
                print("Invalid number. Try again.")
                continue
        except ValueError:
            print("Invalid input. Try again.")
            continue
        else:
            break
    exp = compressList(stringToList(convertStringLower(showString(userString(m))))) 
    testModule.m2(exp)
    print(f'\nThe following is a frequency distribution for the letters in the list.')
    showFrequency(frequencyCount(exp, char, empl), char) 
    return m, char, empl; 


def userString(num): #gets returned value to loop through m inputs and turns the inputted list into string
    line = None
    line = []
    for x in range(1, num + 1):
        print(f'enter string {x}:')
        line.append(input())
    line = str(' '.join(line))
    return line


def showString(lst): #prints inputted string
    print(lst) 
    return lst

def convertStringLower(lst): #converts string into lower all lower case and prints
    nl = lst.lower() 
    print(nl)
    return nl


def stringToList(st): #puts string into list with seperate elements
    ls = list(st)
    return ls

def compressList(lst): #removes spaces in list and prints as a string
    lst = [lst.replace(' ', '') for lst in lst] 
    print(str(''.join(lst)))
    return lst


def frequencyCount(lst, alph, emtl): #loops through each letter and check if an element is part of the list of the letters of the alphabet and adds a 1 to the respective element number in the empty list
    for x in range(len(lst)):
        for y in range(len(alph)):
            if lst[x] == alph[y]:
                emtl[y] += 1
    return emtl 


def showFrequency(lst, alph): #loops through the alphabet and prints an element each iteration along with the number of the empty list multiplied by an asterisk
    for x in range(len(alph)):
        print(alph[x], " ", "*" * lst[x])
    return 0


main()
