import pandas as pd
    
#list of data
lstDances = ["Ballet", "Tap", "Tango", "Square", "Hip-Hop"]
lstNames = [ ["Ballet","Jane"], ["Jazz", "Hadley"], ["Modern", "Lyla"], ["Tap", "London"], ["Tango", "Zoey"], ["Square", "Millie"], ["Hip-Hop", "Beck"]]

#Calling DataFrame constructor on list
dfDance = pd.DataFrame(lstDances)
dfNames = pd.DataFrame(lstNames)

print(dfDance.at[0,0]) #Ballet
print(dfNames.at[0,0]) #Ballet

print(dfDance.at[1,0]) #Tap
print(dfNames.at[1,1]) #Hadley

dfDance.at[4,0] = "Break"
print(dfDance)