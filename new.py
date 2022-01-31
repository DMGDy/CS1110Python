date = input("enter date in mm/dd/yyyy: ")
mm = int(date[0:2])
months = ["January", "February", "March", "April", "May", "June", "July", "August","September", "October", "november", "December"]
month = months[mm-1]
day = int(date[4:5])
print(day)
