#!/usr/bin/python

#Project No.: 06
#Author: Dylan-Matthew Garza
#Description: This program quizzes the user with a user defined filename of spanish words


#importing necessary modules
import re
import random
def main():
    print('Welcome to the vocabulary quiz program. \n ')
    dic     = get_dic(str(input("Please enter a file name: ")))
    print(f'{len(dic)} entries found.') #get from called function
    usrname = str(input("Please enter your full name: "))
    date    = str(input("Please enter the date: "))
    print('\n')
    #Input validation for number of questions
    while 1:
        try:
            number_of_words = int(input("How many words would you like to be quizzed on? "))
            while number_of_words > 11 or number_of_words <= 0:
                number_of_words = int(input("Please enter a valid number between 1 and 10\nHow many words would you like to be quizzed on? "))
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        else:
            break
    random_quiz_list    = random.sample(list(dic.keys()), number_of_words)
    score               = []
    quizdict            = {}
    print(" \n ")
    #beginning quiz for in range of user defined amount
    for x in range(number_of_words):
        #if value contains a comma, it will be handeled differently from a single wword value
        if ',' in dic[random_quiz_list[x]]:
            print(f"English word: {random_quiz_list[x]}")
            w1 = str(input(f"Enter {len(re.findall(',',dic[random_quiz_list[x]])) + 1} equivalent Spanish word(s). Word[1]: "))
            #finds all commas in cases of more than 2 words
            for y in range(len(re.findall(',',dic[random_quiz_list[x]]))):
                w2 = str(input(f"Word [{y+2}]: "))
            if check_quizWords([w1,w2], dic, f'{random_quiz_list[x]}') == True:
                print("Correct!")
                score.append(1)
            else:
                print("Incorrect")
            quizdict[random_quiz_list[x]] = dic.get(random_quiz_list[x])
            print(" \n---\n ")
        else:
            print(f"English word: {random_quiz_list[x]}")
            w = str(input(f"Enter 1 equivalent Spanish word(s). Word[1]: "))
            if check_quizWords([w], dic, f"{random_quiz_list[x]}") == True:
                print("Correct!")
                score.append(1)
            else:
                print("Incorrect")
            quizdict[random_quiz_list[x]] = dic.get(random_quiz_list[x])
            print(" \n---\n ")
    print(f"{len(score)} out of {number_of_words} correct")
    quizdict['Score'] = score
    make_quizFile(usrname, date, quizdict)


def get_dic(file):
    #all in try/except block to prevent FileNotFoundError
    try:
        #takes txt lines to list and seperates elements by : and \n
        with open(file, 'r') as f:
            dic  = {}
            ls   = []
            s1   = re.split(":|\n",''.join(f.readlines()))
            #appends empty list with english words
            for x in range(len(s1)//2):
               ls.append(s1[2*x])
            #creates dictionary values with keys and valye
            for x in range(len(ls)):
                dic[ls[x]] = s1[2*x + 1]
    except FileNotFoundError:
        print(f"The file name {file} does not exist\n \nBye!")
        exit()

    return dic;


def make_quizFile(name, date, quizdic):
    #creates seperate lists from called quiz dictionary
    keys = list(quizdic.keys())
    values = list(quizdic.values())
    outputf = str(input("Enter output file (or press enter to quit): "))
    print("\n Bye!")
    #end program if enter with no input is typed
    if outputf == '':
        exit()
    with open(outputf, 'w') as f:
        f.write(f"Name: {name}\nDate: {date}\n")
        #writes keys and values, -1 to range due to last entry being the score
        for x in range(len(keys) - 1):
            f.write(f"{keys[x]}:{values[x]}\n")
        f.write(f"Score: {len(quizdic.get('Score'))} out of {len(keys) - 1} correct")


def check_quizWords(spaWords, spaDic, engWord):
    #removes all spaces from the keys and list of spanish words
    key = spaDic[engWord].replace(' ','')
    ans = []
    for x in spaWords:
        l = x.replace(' ','')
        ans.append(l)
    #checks if 2 or more words were used in the word
    if len(spaWords) > 1:
        #different combinations of correct answers will still return correct result
        if key == f"{ans[0]},{ans[1]}" or key == f"{ans[1]},{ans[0]}":
            return True
    else:
        if key == ans[0]:
            return True


main()
