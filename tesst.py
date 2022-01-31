import tst

def main():
    myinfo  = tst.PersonalInfo('dy','333', '33', '99')
    myinfo2 = tst.PersonalInfo('dd','4444','21','2121')
    myinfo3 = tst.PersonalInfo('ddd','33333','211','2121')
    myinfo.setAddress('dddsdsdsd')
    print(myinfo.getName(),myinfo.getAddress(),myinfo.getAge(),myinfo.getNumber())
    print(myinfo2.getName(),myinfo2.getAddress(),myinfo2.getAge(),myinfo2.getNumber())

    func1(myinfo.getName(), myinfo.getAddress(),myinfo.getAge(),myinfo.getNumber())
    func1(myinfo2.getName(), myinfo2.getAddress(),myinfo2.getAge(),myinfo2.getNumber())
    func1(myinfo3.getName(), myinfo3.getAddress(),myinfo3.getAge(),myinfo3.getNumber())

def func1(object1, object2, object3):
    object1.set_address('9999 address 0000')



main()
