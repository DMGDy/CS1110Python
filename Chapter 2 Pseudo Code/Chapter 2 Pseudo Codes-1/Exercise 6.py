## 6. Sales Tax
## Write a program that will ask the user to enter the amount of a purchase. The program
## should then compute the state and county sales tax. Assume the state sales tax is 4 percent
## and the county sales tax is 2 percent. The program should display the amount of the purchase, the state sales tax, the county sales tax, the total sales tax, and the total of the sale
## (which is the sum of the amount of purchase plus the total sales tax).
## Hint: use the value 0.02 to represent 2 percent, and 0.04 to represent 4 percent.

sale = input("Enter Sale Amount ")
state = .04 * float(sale)
country = .02 * float(sale)
total = 1.06 * float(sale)
string1 = "State Sales Tax is "
string2 = ", Country Sales Tax is "
string3 = ", fpor a total sales tax of "
string4 = ", for a total of "
print(string1 + str(state) + string2 + str(country) + string3 + str(state + country) + string4 + str(total))
      
