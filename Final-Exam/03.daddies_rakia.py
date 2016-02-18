try:
    import math

    liters_rakia = float(input())
    if liters_rakia < 0:
        raise Exception
    filename = input()
    containers = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            cleanedLine = line.strip()
            if cleanedLine:  # is not empty
                splitted = line.split(',')
                name = splitted[0]
                radius = float(splitted[1])
                height = float(splitted[2])
                if radius <= 0 or height <= 0:
                    raise Exception
                cylinder_volume = math.pi * radius * radius * height
                cylinder_volume_in_liters = cylinder_volume / 1000
                temp_tuple = (name, cylinder_volume_in_liters)
                containers.append(temp_tuple)

    container_name = ''
    minimal = float('Infinity')

    for i in containers:
        liters_diff = i[1] - liters_rakia
        if (liters_diff >= 0 and liters_diff < minimal):
            minimal = liters_diff
            container_name = i[0]

    if container_name:
        print(container_name)
    else:
        print("NO SUITABLE CONTAINER")

except(Exception):
    print("INVALID INPUT")
