def main():
    lst = []
    n = int(input('Enter a Number: '))
    for x in range(2, n):
        prime = True
        for y in range(2, x):
            if x % y == 0:
                prime = False
        if prime == True:
            lst.append(x)
    print(lst)
    return 0


main()
