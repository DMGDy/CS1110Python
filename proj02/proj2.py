tierl = str(["B", "M", "P", "b", "m", "p"])
name = str(input("Enter Employee's Name: "))
base = float(input("Enter Monthly Base: "))
while base < 0:
    print("Inavalid Base Pay")
    base = float(input("Enter Monthly Base: " ))
tier = input("Enter Tier (B, M, or P): ")
while tier in tierl:
    print("Invalid Tier")
