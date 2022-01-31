## 8. Tip, Tax, and Total
## Write a program that calculates the total amount of a meal purchased at a restaurant. The
## program should ask the user to enter the charge for the food, and then calculate the amount
## of a 15 percent tip and 7 percent sales tax. Display each of these amounts and the total.

x = float(input("Price of food: "))
tip = x* 0.15
print("15% tip amount: " + str(tip))
salesTax = x * 0.07
print("SalesTax: " +str(salesTax))
print("Total: " + str(x + salesTax + tip))
