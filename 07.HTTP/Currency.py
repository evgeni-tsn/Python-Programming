import requests

date = input("Дата: ")
currency_from = input("Валута от: ")
amount = input("Сума: ")
currency_to = input("Валута към: ")

response = requests.get('http://api.fixer.io/{}?base={}'.format(date,currency_from))
currency_dict = response.json()

get_current_rate = currency_dict['rates'][currency_to]

result = float(amount)*float(get_current_rate)

print(result)