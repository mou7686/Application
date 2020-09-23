import pandas
df8 = pandas.read_json("supermarkets.json")
df8 = df8.set_index("ID")
df9 = df8.loc[2:3,"Country":"Employees"]
df11 = df8.loc[4,"Name"]
df10 = list(df8.loc[:,"Country"])
print(df10)
