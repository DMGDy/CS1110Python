## 7. Miles-per-Gallon
## A car’s miles-per-gallon (MPG) can be calculated with the following formula:
## Write a program that asks the user for the number of miles driven and the gallons of gas
## used. It should calculate the car’s MPG and display the result.

MilesDriven = float(input("Number of miles driven : " ))
GallonsUsed =float(input("Number of gallons of gas used : "))
MPG = MilesDriven /GallonsUsed
print("MPG = ", format(MPG, '.2f'))
