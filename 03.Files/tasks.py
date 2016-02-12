total_sample = 0
lines_sample = 0

with open('catalog_sample.csv')as f:
    for line in f:
        line = line.split(',')
        total_sample += float(line[-1])
        lines_sample += 1

print("{0:.2f}".format(total_sample/lines_sample))

total_full = 0
lines_full = 0

with open('catalog_full.csv')as f:
    for line in f:
        line = line.split(',')
        total_full += float(line[-1])
        lines_full += 1

print("{0:.2f}".format(total_full/lines_full))