lst = []
for x in range(1,21):
    lst.append(int(input(f'Enter #{x}: ')))
nl = sorted(lst)
print(f'{nl[0]} is the smallest number')
ml = sorted(lst, reverse = True)
print(f'{ml[0]} is the largest number')
print(f'{sum(nl)} is the total of the numbers')
print(f'{float(sum(lst))/20} is the average')

