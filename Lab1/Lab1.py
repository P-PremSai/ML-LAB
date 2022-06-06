import numpy as np
import pandas as pd

data=pd.read_csv("data.csv")
print(data,"\n")

d=np.array(data)[:,:-1]
print("\n The attributes are : ",d)
target=np.array(data)[:,-1]
print("\n Target is : ",target)

def finds(c,t):
    for i,val in enumerate(t):
        if val == "Yes" :
            specific_hypothesis = c[i].copy()
            break
    for i,val in enumerate(c):
        if t[i] == 'Yes' :
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x]= '?'
                else :
                    pass
    return specific_hypothesis 
print("Final hypothesis is : ",finds(d,target))


#Time,Weather,Temperature,Company,Humidity,Wind,Goes
#Morning,Sunny,Warm,Yes,Mild,Strong,Yes
#Evening,Rainy,Cold,No,Mild,Normal,No
#Morning,Sunny,Moderate,Yes,Normal,Normal,Yes
#Evening,Sunny,Cold,Yes,High,Strong,Yes
