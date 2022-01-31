class PersonalInfo:
    def __init__(self, name, address, age, phoneNumber):
        self.__name        = name
        self.__address     = address
        self.__age         = age
        self.__phoneNumber = phoneNumber

    def setName(self, name):
        self.__name        = name


    def getName(self):
        return self.__name
    
    def setAddress(self,address):
        self.__address     = address

    def getAddress(self):
        return self.__address

    def setAge(self, age):
        self.__age         = age
    def getAge(self):
        return self.__age

    def setNumber(self,phoneNumber):
        self.__phoneNumber = phoneNumber
    def getNumber(self):
        return self.__phoneNumber
