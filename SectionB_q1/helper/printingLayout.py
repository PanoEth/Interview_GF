def printLayout(rectangles):

    SCALE = 10 #scale=10 means 10 dots are used to print 1um -> resolution 100nm
    
    if not rectangles:
        print("No shapes added in layout.")
        return

    min_x = int(min(rect.edgeX_left for rect in rectangles))
    max_x = int(max(rect.edgeX_right for rect in rectangles))
    min_y = int(min(rect.edgeY_bottom for rect in rectangles))
    max_y = int(max(rect.edgeY_top for rect in rectangles)) #gathering min and max for vieweing "window"
    width = (max_x-min_x)*SCALE
    height = (max_y-min_y)*SCALE
    grid = [[' ' for _ in range(width)] for _ in range(height)]

    for rect in rectangles:
        if rect.layer == "metal1":
            symbol = '#'
            label = "M1"
        elif rect.layer == "metal2":
            symbol = '*'
            label = "M2"
        else:
            symbol = '.'
            label = "V1"
        #get starting and finishing position for x and y
        start_x = int((rect.edgeX_left-min_x)*SCALE)
        end_x = int((rect.edgeX_right - min_x) * SCALE)
        start_y = int((rect.edgeY_bottom - min_y) * SCALE)
        end_y = int((rect.edgeY_top - min_y) * SCALE)

        #Draw rectangle
        for x in range(start_x, end_x):
            for y in range(start_y, end_y):
                grid[y][x] = symbol

        #Place label in center
        center_x = (start_x+end_x)//2-len(label)//2
        center_y = (start_y+end_y)//2

        for i, ch in enumerate(label):
            if (0 <= center_x + i < width and 0 <= center_y < height):
                grid[center_y][center_x+i] = ch

    print("\nLayout:\n")

    for y in range(height - 1, -1, -1):
        if y % SCALE == 0:
            print(f"{(y // SCALE) + min_y:3} ", end="")
        else:
            print("    ", end="")

        for x in range(width):
            print(grid[y][x], end="")

        print()

    print("    " + "-" * width)
    print("    ", end="")

    for x in range(width):
        if x % SCALE == 0:
            print((x // SCALE + min_x) % 10, end="")
        else:
            print(" ", end="")

    print("\n")
    