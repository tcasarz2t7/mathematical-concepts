import math
def calculate_area(shape):
    if shape == 'circle':
        return math.pi * (radius ** 2)
    elif shape == 'square':
        return size ** 2
    elif shape == 'rectangle':
        return length * width
    else:
        raise ValueError('Invalid shape')
