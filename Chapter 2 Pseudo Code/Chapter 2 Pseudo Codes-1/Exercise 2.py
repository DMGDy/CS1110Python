##2. Sales Prediction
## A company has determined that its annual profit is typically 23 percent of total sales. Write
##a program that asks the user to enter the projected amount of total sales, and then displays
##the profit that will be made from that amount.
##Hint: use the value 0.23 to represent 23 percent.


num = input("Enter your total sale: ")
SaleNum = float(num) * .23
string1 = "Total Profit is "
print(string1 + str(SaleNum))
