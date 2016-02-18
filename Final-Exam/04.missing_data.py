try:
    import iso8601
    from datetime import datetime
    import collections

    result_dict = {}
    all_cities = set()
    isEmpty = True
    with open(input(), encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                splited = line.split(',')
                # //Date format??
                date = iso8601.parse_date(splited[0])
                city = splited[1]
                temperature = splited[2]
                isEmpty = False
                if date not in result_dict.keys():
                    result_dict[date] = set()
                result_dict[date].add(city)
                all_cities.add(city)
    if isEmpty:
        raise Exception

    output_list = []
    od = collections.OrderedDict(sorted(result_dict.items()))

    for date in od:
        diff = result_dict[date]^all_cities
        if diff:
            # NOT SURE
            date_output = date.strftime('%Y-%m-%d') + ','
            sorted_diffs = sorted(diff)
            date_output += ','.join(sorted_diffs)
            output_list.append(date_output)

    if output_list:
        for line in output_list:
            print(line)
    else:
        print('ALL DATA AVAILABLE')
except:
    print("INVALID INPUT")

