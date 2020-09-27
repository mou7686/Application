import pandas
df8 = pandas.read_json("supermarkets.json")
#print(df8)
df9 = df8.set_index("ID")
#print(df9)
df10 = df8.loc[2:3,"Country":"Employees"]
#print(df10)
df11 = df8.loc[4,"Name"]
#print(df11)
df12 = list(df8.loc[:,"Country"])
print(df12)
