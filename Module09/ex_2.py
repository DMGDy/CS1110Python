def main():
    magic_square = [[0,0,0], [0,0,0], [0,0,0]]
    print(f'Enter the numbers for the squares: ')
    for x in range(len(magic_square)):
        for y in range(len(magic_square[x])):
            magic_square[x][y] = int(input(f'row {x + 1}, column {y + 1}: '))
    magic = is_magic(magic_square)
    if magic == True:
        print(f'This is a Magic Square')
    else:
        print(f'This is not a Magic Square')
    return magic_square

def is_magic(sq):
    rowsums = []
    diag = []
    col = []
    rev = []
    for i in zip(*sq):
        col.append(sum(i))
    for x in range(len(sq)):
        rowsums.append(sum(sq[x]))
        for y in range(len(sq[x])):
            if (y == x):
                diag.append(sq[x][y])
    for x in range(len(sq)):
        rev.append(sq[x][len(sq) - (x+1)])
    print(rev)
    if sum(rowsums) == 45 and sum(diag) == 15 and sum(col) == 45:
        return True
    else:
        return False
main()
