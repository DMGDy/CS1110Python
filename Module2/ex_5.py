P = float(input("Original amount of principal deposited? "))
r = float(input("Percent interest rate? ")) / 100
n = float(input("Number of times per year interest is compounded?(4 or 12) "))
t = float(input("Number of years interest will be compounded? "))
A = P * (1 + r * n) * (n * t)
A_f = "{:.2f}".format(A)
print("There will be $" + str(A_f) + " in the account")
print(str(r))
