def main():
    tier_l = ["B","M","P","b","m","p"]
    name = str(input("Enter Employee's Name: "))
    base = float(input("Enter Monthly Base: "))
    while base < 0:
        print("Inavalid Base Pay")
        base = float(input("Enter Monthly Base: " ))
    tier = input("Enter Tier (B, M, or P): ")
    while tier not in tier_l:
        print("Invalid Tier")
        tier = input("Enter Tier (B, M, or P): ")
    sold = int(input("Enter Items Sold: "))
    while sold < 0:
        print("Invalid number for Items Sold")
        sold = int(input("Enter Items Sold: "))
    if tier == "B" or tier == "b":
        if sold in range(10,15):
            base += sold * 50
        if sold > 15:
            base += sold * 75
        if sold < 10:
            print("WARNING: Sales must improve.")
    if tier == "M" or tier == "m":
        if sold in range(15,21):
            base += sold * 60
        if sold > 20:
            base += sold * 100
        if sold < 15:
            print("WARNING: Sales must improve to stay in tier M")
    if tier == "P" or tier == "p":
        if sold in range(20,26):
            base += sold * 75
        if sold > 25:
            base += sold * 125
        if sold < 20:
            print("WARNING: Sales must improve to stay in tier P")
    print (name + ", Tier: " + tier + ", Sold " + str(sold) + " items, Monthly Payment: " + str(base))
    print("")
    anslst = ['y','Y','N','n']
    another = input("Do you want to enter another employee? ")
    anchr = another[0]
    if anchr not in anslst:
        print("Invalid Answer")
        another = input("Do you want to enter another employee? ")
        anchr = another[0]
    elif anchr == "N" or anchr == "n":
        exit()
while True:
    main()
