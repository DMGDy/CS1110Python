my_tuple = (1, 3, 0, 2, 5, 6, 9, 10, 7, 0)
print(f'my_tuple = {my_tuple}\n')
#Subscript indexing
print(f'my_tuple[4] = {my_tuple[4]}\n')

#Tuple Methods

#counting
print(f'my_tuple.count(0) = {my_tuple.count(0)}')
#index
print(f'my_tuple.index(10) = {my_tuple.index(10)}\n')

#Built-in functions

#len
print(f'len(my_tuple) = {len(my_tuple)}')
#min
print(f'min(my_tuple) = {min(my_tuple)}')
#max
print(f'max(my_tuple) = {max(my_tuple)}\n')

#Slicing Expressions
print(f'Last 4 elements, my_tuple[6:] = {my_tuple[6:]}\n')

#The in operator
if 5 in my_tuple:
    print(f'value 5 exists in the tuple\n')
else:
    print(f'value 5 does not exist in the tuple\n')

#The + and * operator
my_tuple += (8,)
print(f'my_tuple += (8,)\nprint(my_tuple) = {my_tuple}\nprint(my_tuple*2) = {my_tuple*2}')
