def fill_the_box(height, length, width, *args):
    volume = height * length * width
    boxes_left = 0
    for box in args:
        if box == "Finish":
            break
        if volume >= box:
            volume -= box
        else:
            boxes_left += box - volume
            volume = 0
    if volume:
        return f"There is free space in the box. You could put {volume} more cubes."
    else:
        return f"No more free space! You have {boxes_left} more cubes."


print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))