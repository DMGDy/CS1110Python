## 3. Land Calculation
## One acre of land is equivalent to 43,560 square feet. Write a program that asks the user to
## enter the total square feet in a tract of land and calculates the number of acres in the tract.
## Hint: divide the amount entered by 43,560 to get the number of acres.

totalSquareFeet = float(input("Enter the total square feet: "))
print("Total acres in the tract: " + str(totalSquareFeet/43560)
)
