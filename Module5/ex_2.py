def main():
    print("Enter the replacement cost of the building: ")
    cost = float(input())
    minVal = est(cost)
    print("The minimum amount of insurance you should buy for the property is ", minVal)
def est(x):
    cst = x * .8
    return cst
main()
