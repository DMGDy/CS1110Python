mtr = ([4, 9, 2], [3, 5, 7], [8, 1, 6])
for x in range(3):
    print(f'{sum(mtr[x])} is the sum of the {x+1} row')
for y in range(len(mtr)):
	print(f'{mtr[0][0] + mtr[1][1] + mtr[2][2]} is the sum of the diagnals')

