import sys
try:
    try:
        print(x)
    except:
        print("We have a problem, please contact technical support.")

    try:
        print(x)
    except:
        print("We have a problem with y. please contact technical support.")
    
    print(x+z)
except: 
    print("Big Problem!")
    sys.exit()
finally: 
    print("I am done")

print("I am still running.")