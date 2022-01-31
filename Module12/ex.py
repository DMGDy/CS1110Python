import pickle

class Employee:
    def __init__(self, name, IDnum, dep, job):
        self.__name     = name
        self.__IDnum    = IDnum
        self.__dep      = dep
        self.__job      = job
        pass
    def set_name(self,name):
        self.__name     = name
        return 
    def get_name(self):
        return self.__name
    def set_ID(self, IDnum):
        self.__IDnum    = IDnum
        return
    def get_ID(self):
        return self.__IDnum

    def set_dep(self, dep):
        self.__dep      = dep
        return
    def get_dep(self):
        return self.__dep
    def set_job(self, job):
        self.__job      = job
        return
    def get_job(self):
        return self.__job
    pass

def main():
    try:
        with open("dic","rb") as f:
           dic = pickle.load(f)
    except FileNotFoundError:
        dic = {}
    print("Press:\nl to list current employees\na to add a new employee\nc to change the information of an employee\nd to remove an employee\nq to quit")
    inp = None
    while (1):
        inp = str(input("Enter a command (l,a,c,d,q): "))
        if inp == "l":
            print(dic)
        if inp == "a":
            name = str(input("Enter employee name: "))
            locals()[name] = Employee(name ,str(input("Enter employee ID: ")),str(input("Enteremployee department: ")), str(input("Enter employee job: ")) )
            dic[locals()[name].get_name()] = locals()[name].get_ID()
            print(dic)
        if inp == "c":
            name = str(input("enter the name of the employee you would like to change: "))
            while name not in dic:
                name = str(input("Employee does not exist with that name. Enter a valiod name: "))
            locals()[name].set_name(str(input("set employee new name: ")))
            locals()[name].set_ID(str(input("Set new ID: ")))
            locals()[name].set_dep(str(input("Set new department: ")))
            locals()[name].set_job(str(input("Set new job: ")))
            dic.pop(name)
            dic[locals()[name].get_ID()] = locals()[name].get_name()
            print(dic)
        if inp == "d":
            name = str(input("Enter the name of the user you want to delete: "))
            dic.pop(name)
        if inp == "q":
            with open("dic","wb") as f:
                pickle.dump(dic,f)
                print("exiting program...")
                exit()





main()
