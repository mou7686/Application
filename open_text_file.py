import pandas
df4 = pandas.read_csv("supermarkets-semi-colons.txt")
df5 = pandas.read_csv("supermarkets-semi-colons.txt",sep=";") # sep=separator

print(df4)
print(df5)