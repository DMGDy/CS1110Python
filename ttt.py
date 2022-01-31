import math
print(math.pi)
x = list(range(1,5))

try:
    for i in range(0,3):
        if i == 0:
            print(y[i])
        elif i == 1:
            5/0
        else:
            print(x[4])
except NameError as e:
    print('wrong1')
except ZeroDivisionError as e:
    print('wrong2')
except IndexError as e:
    print('wrong3')
