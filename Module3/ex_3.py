mass = float(input("Enter the mass of the object: "))
weight = mass * 9.8
print(str(weight) + " N")
if weight < 500:
    print("The object is too heavy")
if weight in range(0,100):
    print("the obejct is too light")
