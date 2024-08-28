import pandas as pd
    
#list of data
lstDances =  ["Ballet", "Jazz", "Modern", "Tap", "Tango", "Square", "Hip-Hop"]
lstNames =   [["Ballet","Jane"], ["Jazz","Hadley"], ["Modern","Lyla"], ["Tap","London"],["Tango", "Zoey"], ["Square","Millie"],["Hip-Hop", "Beck"]]
            

#Calling DataFrame constructor on list
dfDance = pd.DataFrame(lstDances)
dfNames = pd.DataFrame(lstNames)

print(dfDance.at[4,0])
print(dfNames.at[1,1])

dfDance.at[4,0] = "Break"
print(dfNames)
dfNames.at[6,0] = "Break"
print(dfNames)