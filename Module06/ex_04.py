def main1():
    name = None
    print(f'Enter the name of the player whos score you would like to modify')
    name = input()
    f = open('golf.txt','r')
    index = 0
    found = 0
    for line in f:
        index += 1
        if name in line:
            found = 1
            break
    if found == 0:
        print(f'invalid name')
    if found == 1:
        index += 1
    f.close()
    n_score = None
    print("Enter the new score: ")
    n_score = int(input())
    f = open('golf.txt','r')
    ls = f.readlines()
    ls[index] = f'score: {n_score}\n\n'
    f = open('golf.txt','w')
    f.writelines(ls)
    f.close()



main1()
