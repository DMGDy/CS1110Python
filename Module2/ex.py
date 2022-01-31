stocks = float(2000)
sharec = float(40.00)
com = float(0.03)
nsharec = float(42.75)
totalc = stocks * sharec
comt = totalc * com
ntotalc = stocks * nsharec
ncomt =  ntotalc * com
prof = (ntotalc - (ncomt + comt + totalc))
print("Joe has paid a total of $" + str(totalc) + " for the stock.")
print("He paid a commission of $" + str(comt) + " to his broker")
print("Joe later sold the stock for $" + str(ntotalc))
print("He paid another commision of $" + str(ncomt))
print("Joe has made a profit of $" + str(prof))
if prof > 0:
    print("Joe has made a profit")
else:
    print("Joe has lost money")

