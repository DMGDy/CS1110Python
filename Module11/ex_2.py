class Car:
    def __init__(self,year_model,make,speed):
        self.__year_model       = year_model
        self.__make             = make
        self.__speed            = speed
        pass
    def accelerate(self):
        self.__speed += 5
        return
    def brake(self):
        self.__speed -= 5
        return
    def get_speed(self):
        return self.__speed


def main():
    car = Car("2000","x", 0)
    for x in range(5):
        car.accelerate()
        print(car.get_speed())
    for x in range(5):
        car.brake()
        print(car.get_speed())




main()
