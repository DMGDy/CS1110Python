## 4. Total Purchase
## A customer in a store is purchasing five items. Write a program that asks for the price of
## each item, and then displays the sub

num1 = float(input("enter item 1: "))
num2 = float(input("enter item 2: "))
num3 = float(input("enter item 3: "))
num4 = float(input("enter item 4: "))
num5 = float(input("enter item 5: "))
befTax = num1 + num2 + num3 + num4 + num5
taxRate = befTax * .06
afterTax = befTax * 1.06
string1 = "additional tax is "
string2 = ", for a total of "
print(string1 + str(taxRate) + string2 + str(afterTax))
