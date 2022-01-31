number = int(input("Starting number of organisms: "))
incr = str(input("Average daily increase: "))
increase = float(incr[:-1]) 
print(str(increase))
days = int(input("Number of days to multiply: " ))
print("Day    Approximate population")
print("1","    ",str(number))
for i in range(1,days):
    number += (increase/100) * number
    numberf = "{:.2f}".format(number)
    print(i+1,"    ", str(numberf))
