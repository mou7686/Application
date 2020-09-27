import pandas
df8 = pandas.read_json("supermarkets.json")
df8 = df8.set_index("ID")
df9 = df8.drop("City",1)
df10 = df8.drop(1,0) # 1 is for ID 1 and 0 is for rows
df11 = df8.drop(df8.index[0:3],0) # 0 For rows
df12 = df8.drop(df8.columns[0:3],1) # 1 for columns
df13 = df8.index
df14 = df8.columns
#print(df9)
#print(df10)
#print(df11)
#print(df12)
#print(df13)
print(df14)