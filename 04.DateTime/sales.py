import csv
import operator
from datetime import datetime

prices_per_day = {}  # dict
with open('sales.csv', 'r') as f:
    reader = csv.reader(f)
    sales_in_list = list(reader)
    for i in sales_in_list:
        splitted = str(i).split(',')
        get_date = datetime.strptime(splitted[0][2:-10], '%Y-%m-%d')
        get_price = splitted[1][2:-2]
        if get_date in prices_per_day:
            prices_per_day[get_date] += float(get_price)
        else:
            prices_per_day[get_date] = float(get_price)

sorted_x = sorted(prices_per_day.items(), key=operator.itemgetter(1))

for key, value in sorted_x:
    print("{} --> {:.2f}".format(str(key)[0:-9], value))

print("---------------")
print("Day with max sales")
max_element_date = max(prices_per_day.items(), key=operator.itemgetter(1))[0]
max_element_price = max(prices_per_day.items(), key=operator.itemgetter(1))[1]
print('{} --> {:.2f}'.format(str(max_element_date)[0:-9], max_element_price))
