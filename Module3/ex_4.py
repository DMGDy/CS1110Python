num = int(input("Enter the number you would like to find the factorial of: "))
fac = 1
if fac <= 0:
    print("invalid number")
for i in range(1, num + 1):
    fac = fac * i
print(fac)
