def main():
    try:
        f = open('golf.txt','a')
    except IOError:
        f = open('golf.txt', 'w')
    print(f'Enter your name: ')
    name = input()
    print(f'Enter your score: ')
    score = input()
    f.write(f'\nname: {name}\nscore: {score}\n\n')
    f.close()




main()
