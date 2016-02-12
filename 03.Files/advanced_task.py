# Sums
infant_sum = 0
kid_sum = 0
men_sum = 0
unisex_sum = 0
woman_sum = 0

# Counters
infant_count = 0
kid_count = 0
men_count = 0
unisex_count = 0
woman_count = 0
with open('catalog_sample2.csv')as f:
    for line in f:
        line = line.split(',')
        if line[-2] == 'Infant':
            infant_sum += float(line[-1])
            infant_count += 1;
        elif line[-2] == 'Kid':
            kid_sum += float(line[-1])
            kid_count += 1
        elif line[-2] == 'Men':
            men_sum += float(line[-1])
            men_count += 1
        elif line[-2] == 'Woman':
            woman_sum += float(line[-1])
            woman_count += 1
        elif line[-2] == 'Unisex':
            unisex_sum += float(line[-1])
            unisex_count += 1

# Output
print('{0:.2f}'.format(infant_sum / infant_count))
print('{0:.2f}'.format(kid_sum / kid_count))
print('{0:.2f}'.format(men_sum / men_count))
print('{0:.2f}'.format(woman_sum / woman_count))
print('{0:.2f}'.format(unisex_sum / unisex_count))
