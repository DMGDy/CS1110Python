print("*******************************")
print(" ")
gallons = float(input("Please enter the number of gallons of gasoline: " ))
print(" ")
print("The number of gallons you entered is: " + str(gallons))
liters = 3.7854 * gallons
barrels = gallons / 19.5
ethenol = (gallons * 115000) / 75700
dollars = float(str(int(4 * gallons)))
g = str(gallons) + " gallons of gasoline"
print(g + " = " + str(liters) + " liters")
print(g + " requires " + str(barrels) + " barrels of oil")
print(g + " has an energy = " + str(ethenol) + " gallons of ethenol")
print(g + " requires " + str(dollars) + " US dollars")
print(" ")
print("************The End************")
