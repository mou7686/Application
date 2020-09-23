import pandas
df6 = pandas.read_csv("data.txt",header=None)
df6.columns = ["ID", "Address", "City", "ZIP", "Country", "Name", "Employees"]
df7 = df6.set_index("ID",inplace=True)

print(df6)
