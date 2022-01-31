def main():
    search_term = None
    print("search: ")
    search_term = input()
    f = open('golf.txt','r')
    index = 0
    found = 0
    for line in f:
        index += 1
        if search_term in line:
            found = 1
            break
    if found == 0:
        print(f'did not find: {search_term} ')
    if found == 1:
        print(f'found: {search_term} on line {index}')
    f.close()
    return index

main()

