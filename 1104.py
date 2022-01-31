sales = []
for x in range(1, 8):
    sales.append(float(input(f'enter day {x}: ')))
print(f'${sum(sales)} is the total sales for the week')
