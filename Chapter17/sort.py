import numpy as np
import pandas as pd
            
#list of data
lstNames =  {   "Type" : [ np.nan, "Jazz", "Modern", "Tap", "Tango", "Square", "Hip-Hop"],
                "Dancer" : ["Jane", np.nan, "Lyla", "London", "Zoey", "Millie", "Beck"],
                "Age" : [18, 23, 19, 20, 21, 22, 21]
            }

#Calling DataFrame constructor on list
dfDance = pd.DataFrame(lstNames)

#Clean the Data and replace np.nan with ""
dfDance =dfDance.fillna("")    

dfDance.sort_values(["Age", "Dancer"] , ascending=(False, True) , inplace=True)

print(dfDance)