GAL_LITERS= 3.7854
USDOLLARS= 4.00
BARREL= 19.5
GALBTU= 75700

print('*******************************')
print()
gallons= input('Please enter the number of gallons: ')
floatVar= float(gallons)
print('The number of gallons of gasoline you entered is: ', floatVar)
print()
galonsToLiters= floatVar*GAL_LITERS
print(floatVar,  'gallons of gasoline =', galonsToLiters,' liters')
gallonsToBarrel= floatVar/BARREL
print(floatVar,  'gallons of gasoline requires', gallonsToBarrel,' barrels of oil')
gallonsToBTU= (floatVar*115000)/GALBTU
print(floatVar,  'gallons of gasoline has an energy = ', gallonsToBTU,' gallons of ethanol')
price= floatVar*USDOLLARS
print(floatVar,  'gallons of gasoline requires', price,' US dollars')
print()
print('************The End************')


