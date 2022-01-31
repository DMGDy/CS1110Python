def main():
    n = int(input("Enter the dimension for the n x n Matrix: "))
    magic_square = [[0 for i in range(n)] for j in range(n)]
    for x in range(n):
        for y in range(n):
            magic_square[x][y] = int(input(f' row {x + 1}, column {y + 1}: '))
    print(magic_square)
    magic = is_magic(magic_square, n)
    if magic == True:
        print(f'This is a Magic Square')
    else:
        print(f'This is not a Magic Square')
    return magic_square

def is_magic(sq, n):
    row = []
    diag = []
    col = []
    rev = []
    for i in zip(*sq):
        col.append(sum(i))
    for x in range(len(sq)):
        row.append(sum(sq[x]))
        for y in range(len(sq[x])):
            if (y == x):
                diag.append(sq[x][y])
    for x in range(len(sq)):
        rev.append(sq[x][len(sq) - (x + 1)])
    if sum(row) == n * sum(diag) == sum(col) == n * sum(rev):
        return True
    else:
        return False
main()
