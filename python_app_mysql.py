import mysql.connector

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
) #use a variable to store the connection.

cursor = con.cursor()

word = input("Enter a word :").lower()

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '{}'".format(word)) # * is used for all
results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    print("No word found!")