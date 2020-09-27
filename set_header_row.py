import pandas
df6 = pandas.read_csv("data.txt",header=None) # At the top header come 0 1 2..because of header=none
#print(df6)
df6.columns = ["ID", "Address", "City", "ZIP", "Country", "Name", "Employees"]
#print(df6)
df6.set_index("ID",inplace=True) # To set ID as an index permenently

print(df6)
