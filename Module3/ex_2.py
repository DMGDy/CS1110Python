age = int(input("Enter your age: "))
if age in range(-1,2):
    print("You are an infant")
if age in range(2,14):
    print("You are a child")
if age in range(14,20):
    print("you are a teenager")
if age >= 20:
    print("You are an adult")
