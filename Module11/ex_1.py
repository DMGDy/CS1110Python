class Pets:
    def __init__(self,name, animal_type, age):
        self.__name        = name
        self.__animal_type = animal_type
        self.__age         = age
        pass
    
    def set_name(self,name):
        self.__name        = name
        return
    def return_name(self):
        return self.__name

    def set_animal_type(self,animal_type):
        self.__animal_type = animal_type
        return
    def get_animal_type(self):
        return self.__animal_type

    def set_age(self,age):
        self.__name        = age
        return
    def get_age(self):
        return self.__name
    pass
def main():
    usr = Pets(str(input("name of pet? ")), str(input("type of animal of pet? ")), str(input("age of pet? ")))

    print(f"{usr.get_animal_type()}\n{usr.return_name()}\n{usr.get_age()}")

main()

