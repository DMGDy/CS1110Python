item_1 = float(input("item 1 cost? "))
item_2 = float(input("item 2 cost? "))
item_3 = float(input("item 3 cost? "))
item_4 = float(input("item 4 cost? "))
item_5 = float(input("item 5 cost? "))
subtotal = str(item_1+item_2+item_3+item_4+item_5)
print("subtotal is " + subtotal)
print("with 6% sales taxes, the total cost is:")
print(float(subtotal)*1.06)