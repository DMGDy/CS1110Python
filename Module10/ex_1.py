with open('file1.txt', 'r') as f1, open('file2.txt', 'r') as f2:
    x = set(str(''.join(f1.readlines())).lower().strip().replace(',','').replace('.','').split())
    y = set(str(''.join(f2.readlines())).lower().strip().replace(',','').replace('.','').split())
    print(f'The difference between the two text files:\n{list(x^y)}')
    print(f'\nWords that appear in both sets:\n{list(x&y)}')
    print(f'\n Words that are unique in the first text:\n{list(x - y)}')
    print(f'\n Words that are unique in the second text:\n{list(y -x)}')
    print(f'\n Words that appear in either but not both:\n{list((x-y)|(y-x))} ')
