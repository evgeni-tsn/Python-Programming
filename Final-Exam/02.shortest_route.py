try:
    filename = input()
    starting_x = 0
    starting_y = 0
    with open(filename, encoding="utf-8") as f:
        isMoved = False
        for line in f:
            cleanedLine = line.strip()
            if cleanedLine:  # is not empty
                splitted = line.split()
                direction = splitted[0]
                step = float(splitted[1])
                if direction == 'right':
                    isMoved = True
                    starting_x += step
                elif direction == 'left':
                    isMoved = True
                    starting_x -= step
                elif direction == 'up':
                    isMoved = True
                    starting_y += step
                elif direction == 'down':
                    isMoved = True
                    starting_y -= step
    if isMoved:
        print("X {:.3f}".format(starting_x))
        print("Y {:.3f}".format(starting_y))
    else:
        print("INVALID INPUT")
except:
    print("INVALID INPUT")
