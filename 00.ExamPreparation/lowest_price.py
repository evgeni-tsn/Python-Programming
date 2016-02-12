
needed_item = input()
filename = input()

items_list = []
with open(filename, encoding="utf-8") as f:
    for line in f:
        splited = line.replace('"', '').split(',')
        item_id = splited[0]
        country = splited[2]
        price = splited[-1].replace("\n", "")
        item_tuple = (item_id, country, price)
        items_list.append(item_tuple)

min_price = float('Infinity')
city = ''
for item in items_list:
    if item[0] == needed_item:
        if float(item[2])<min_price:
            min_price = float(item[2])
            city = item[1]

print(city)