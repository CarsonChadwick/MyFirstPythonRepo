#for icount in range(1,10,2) :
   #print (icount, end=" ")

# Create Variables
lstEvens = []
lstOdds = []
icount = 0

# While Loop
while (icount < 11):
    # Test to see if is even or odd and store to a list
    if (icount/2).is_integer():
        lstEvens.append(icount)
    else :
        lstOdds.append(icount)
    # Print Statement for last loop of the while
    if (icount == 10) :
        for iNum in range(0, len(lstEvens)) :
               print(lstEvens[iNum], end= " ")
        print("")
        for iNum in range(0, len(lstOdds)) :
              print(lstOdds[iNum], end=" ")
    # Increment counter
    icount += 1



