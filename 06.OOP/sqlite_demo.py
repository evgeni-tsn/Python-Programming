import sqlite3

connection = sqlite3.connect('../sales-example.db')
print("Connected")

cursor = connection.cursor()
cursor.execute('SELECT * FROM catalog WHERE category = "SHOES"')
results = cursor.fetchall()
print(results)
