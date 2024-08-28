def func1() :
    print("call func2")
    func2()
    print("leaving func 1")
def func2() :
    print("call func3")
    func3()
    print("leaving func 2")
def func3() :
    print("call func4")
    func4()
    print("leaving func 3")
def func4() :
    print("leaving func 4")

print("This is the main part of the program")
func1()