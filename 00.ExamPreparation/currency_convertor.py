exchange_filename = input()
amounts_filename = input()

with open(exchange_filename, encoding="utf-8") as f:
    exchange_rates_dictionary = dict([line.split() for line in f])

with open(amounts_filename, encoding="utf-8") as f:
    for line in f:
        splited_items = line.split()
        if exchange_rates_dictionary[splited_items[1]]:
            print("{:.2f}".format(float(splited_items[0]) / float(exchange_rates_dictionary[splited_items[1]])))




