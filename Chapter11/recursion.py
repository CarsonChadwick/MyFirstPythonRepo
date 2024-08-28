# Carson Chadwick
# Section 04
# Practice Recursion addin numbers 4,3,2,1

def add_Numbers (iNum) :
    if (iNum == 0) :
        return iNum
    else: 
        iSum = iNum + (add_Numbers(iNum-1))
    return iSum
iNum = 5
print("The sum of " + str(iNum) + " and each consecutive lower numeber is " + str(add_Numbers(iNum)))