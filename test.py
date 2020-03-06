import pandas as pd 

df=pd.read_csv("visual.csv")
zomato=pd.read_csv("/home/vaishnavi/Downloads/zm.csv")
d=['book_table','cuisines']
print(d)
zomato.head()
column_1 = zomato[d[0]]
column_2 = zomato[d[1]]
correlation = column_1.corr(column_2)
print(str(correlation))