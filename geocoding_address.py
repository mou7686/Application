import pandas
df = pandas.read_csv("supermarkets.csv")
df["Address"] = df["Address"]+", "+df["City"]+", "+df["State"]+", "+df["Country"]
from geopy.geocoders import ArcGIS
nom = ArcGIS()
df["Coordinates"] = df["Address"].apply(nom.geocode)
n=df.Coordinates
m=df.Coordinates[0]
o=df.Coordinates[0].latitude
p=df.Coordinates[0].longitude
df["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
df["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude if x != None else None)
#print(df)
#print(n)
#print(m)
#print(o)
#print(p)
print(df)