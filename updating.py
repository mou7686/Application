import pandas
df8 = pandas.read_json("supermarkets.json")
df10 = df8.set_index("ID")
df9 = df8.shape #it indicates 6 rows and 7 columns
#df9 = df8.shape[0] it indicates 6rows only
df10["Continent"] = df8.shape[0]*["North America"] #adding columns
df10["Continent"] = df8["Country"] + "," + "North America"
df11 = df10_t = df10.T #it converts rows into column and column into rows i.e. transpose
df11["My Address"] = ["my city","my country",10,7,"my shop","my state","my continent"]
df11 = df11_t = df11.T 
#print(df10)
#print(df9)
#print(df10)
#print(df10)
#print(df11)
#print(df11)
print(df11)