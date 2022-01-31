lst = []
for x in range(1,21):
    lst.append(int(input(f'Enter #{x}: ')))
nl = sorted(lst)
ml = sorted(lst, reverse = True)
print(f'{nl[0]} is the smallest number,\n {ml[0]} is the largest number, \n {sum(nl)} is the total of the numbers, \n and {float(sum(lst))/20} is the average')
