def main():
    print("How much grams of fat consumed? ")
    fat = float(input())
    print("How much grams of carbohydrates are consumed? ")
    carbs = float(input())
    calories = conv(fat)
    print("The amount of calories consumed from fat is ", calories)
def conv(x):
    cal = x * 9
    return cal
main()
