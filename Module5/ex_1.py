def main():
    print("Enter distance in kilometers: ")
    kilometers = float(input())
    miles = conv(kilometers)
    print("The distance in miles is ", miles)

def conv(x):
    dist = x * 0.6214
    return dist
main()


