import math

try:
    volume_of_one_sheet = float(input())
    a = float(input())
    b = float(input())
    c = float(input())
    needed_volume_for_pack = 2*(a*b + a*c + b*c)*1.098
    result = (needed_volume_for_pack / volume_of_one_sheet)
    print(math.ceil(result))
    # 0.80  1.23  0.78  0.50 
except:
    print("INVALID INPUT")