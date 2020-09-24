import numpy as np
import pandas as pd
from apyori import apriori
#read the data set store_data which contain transaction history of items in a supermarket
data = pd.read_excel('C:\\Users\\Ravi Kumar\\Desktop\\Store_dataset.xlsx')
#For apriori algorithm we need the data set in list format
records = []
for i in range(0, 7501):
    records.append([str(data.values[i,j]) for j in range(0, 20)])
    
association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
association_results = list(association_rules)

print(len(association_results))
print(association_results[0])

#Printingg rules
for item in association_results:
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
    
    
#support=no of transaction contain a particular item/total no of transaction
#confidence=no of transaction where a and b bought togethor/Total no of transaction of a
#Lift=confidence(a->b)/support(b)