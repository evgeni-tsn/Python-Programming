total_time = 0

with open(input(), encoding="utf-8") as f:
    for line in f:
        splited = line.split(',')
        kilometers_from = float(splited[0])
        kilometers_to = float(splited[1])
        speed = float(splited[2].replace("\n", ''))

        distance = kilometers_to - kilometers_from + 1
        time = distance / speed
        total_time+=time

print("{:.2f}".format(total_time))

