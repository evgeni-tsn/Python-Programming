import math
try:
    width = float(input())
    height = float(input())
    area = width*height
    result = area/1.76
    print(math.ceil(result))
except:
    print("INVALID INPUT")