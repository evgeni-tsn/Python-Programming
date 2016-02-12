import collections
input_string = input()
most_common_char = collections.Counter(input_string).most_common(1)[0]
print(most_common_char[0])