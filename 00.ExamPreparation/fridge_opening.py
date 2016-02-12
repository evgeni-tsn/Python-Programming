import csv

results = []
with open(input(), newline='') as csvfile:
    r = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in r:
        currentDate = row[0]
        currentTemperature = row[1]
        temp_tuple = (currentDate, float(currentTemperature))
        results.append(temp_tuple)

default_temp = results[1][1]
for entry in results:
    if entry[1]-default_temp>4:
        print(entry[0])
    default_temp = entry[1]