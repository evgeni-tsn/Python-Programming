price_list = []


def checkEqual(iterator):
	return len(set(iterator)) <= 1

while True:
	price = input("Enter price:")
	if price == 'stop':
		break
	price_list.append(float(price))
if checkEqual(price_list):
	print("All prices are the same.")
elif len(price_list) < 3:
	print("We need more prices.")
else:
	price_list.sort()
	price_lowest = price_list[0]
	while price_list == price_lowest and price_list:
		price_list.pop(0)

	price_highest = price_list[-1]
	while price_list == price_highest and price_list:
		price_list.pop(-1)

	average_price = sum(price_list) / float(len(price_list))
	print(price_list)
	print(average_price)
