def calculate_area(shape):
    if shape == "circle":
        radius = float(input("What is the radius of the circle?"))
        return 3.14 * (radius ** 2)
    elif shape == "square":
        side = float(input("What is the length of a side of the square?"))
        return side ** 2
    elif shape == "rectangle":
        width = float(input("What is the width of the rectangle?"))
        height = float(input("What is the height of the rectangle?"))
        return width * height
    else:
        raise ValueError("Invalid shape")
