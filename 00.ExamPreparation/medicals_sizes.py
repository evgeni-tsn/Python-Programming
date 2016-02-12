try:
    box_width = float(input())
    box_height = float(input())
    box_depth = float(input())
    filename = input()
    box_sizes = [box_depth, box_height, box_width]
    box_sizes.sort()

    with open(filename, encoding="utf-8") as f:
        for line in f:
            split_line = line.split(',')
            medical_width = float(split_line[1])
            medical_height = float(split_line[2])
            medical_depth = float(split_line[3])

            medical_list = [medical_height, medical_depth, medical_width]
            medical_list.sort()

            if medical_list[0] < box_sizes[0] and medical_list[1] < box_sizes[1] and medical_list[2] < box_sizes[2]:
                print(split_line[0])

except:
    print("INVALID INPUT")