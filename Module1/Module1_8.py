cost = float(input("Total cost of meal? "))
taxed = cost*1.07
tip = taxed*0.15
print("The total amount after a 7% sales tax then a 15% tip is " + str(taxed + tip))
