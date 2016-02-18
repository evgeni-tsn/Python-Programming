try:
    filename = input()

    cities_dict = dict()
    sales_dict = dict()
    isEmpty = False
    with open(filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:  # is not empty
                splitted = line.split(',')
                id = splitted[0].strip('"')
                city = splitted[2].strip('"')
                isEmpty = True
                if id not in sales_dict:
                    sales_dict[id] = []
                if city not in cities_dict:
                    cities_dict[city] = []
                sales_dict[id].append(city)
                cities_dict[city].append(id)
    if not isEmpty:
        raise Exception

    sorted_cities = sorted(cities_dict.keys(), reverse=False)
    actual_output = list()

    for city in sorted_cities:
        formatted_output = city
        items = []
        isAdded = False
        for sale in cities_dict[city]:
            if len(sales_dict[sale]) == 1:
                isAdded = True
                items.append(',' + sale)
        sorted_items = sorted(items, reverse=False)
        for each in sorted_items:
            formatted_output += each
        if isAdded:
            actual_output.append(formatted_output)
    if actual_output:
        for line in actual_output:
            print(line)
    else:
        print('NO UNIQUE SALES')
except:
    print("INVALID INPUT")
