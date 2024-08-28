import pandas as pd

#list of data
#list of data
lstNames = { "Type" : ["Ballet", "Jazz", "Modern", "Tap", "Tango", "Square", "Hip-Hop"],
                "Dancer" : ["Jane", "Hadley", "Lyla", "London", "Zoey", "Millie", "Beck"],
                "Age" : [18, 23, 19, 20, 21, 22, 21]
            }

#Calling DataFrame constructor on list
dfDance = pd.DataFrame( lstNames, index = [1,2,3,4,5,6,7])

print(dfDance)