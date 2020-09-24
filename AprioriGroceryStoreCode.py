import numpy as np
import pandas as pd
from apyori import apriori

df=pd.read_excel(open('C:\\Users\\Ravi Kumar\\Desktop\\Groceries_dataset.xlsx','rb'))

#convert data in the form of list
record=[]
for i in range(0,19):
    record.append([str(df.values[i,j]) for j in range(0,4)])

#build apriori model

ass_rule=apriori(record,min_support=0.50,min_confidence=0.40,min_lift=0.5,min_length=2)
ass_result=list(ass_rule)

#print the number of rule generated
print(len(ass_result))

#check the rule

print(ass_result)
