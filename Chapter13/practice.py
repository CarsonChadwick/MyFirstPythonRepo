try: 
    import MyLibrary

    iCount = 245
    iNumTests = 0

    sName = "Alfalfa"
    fAve = iCount/iNumTests

    print(fAve)

    print(sName[15])
    fNewFile = open("test")
except PermissionError: 
        print("Not a valid file.")
except ModuleNotFoundError:
    print("You can not import this library")
except ZeroDivisionError :
    print("Can not divide by zero.")  
except NameError:
    print("Invalid name.")
except IndexError :
    print("Wrong index")