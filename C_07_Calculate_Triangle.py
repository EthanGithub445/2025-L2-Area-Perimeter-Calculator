# Function to calculate for triangle
def calculate_triangle(a, b, c, height):
    # Area using half base x height
    area = 0.5 * (b * height)

    # Perimeter by adding all sides (side b for base)
    perimeter = a + b + c
    return ["Triangle", f"Sides={a}, {b}, {c}, Height={height}", (area, 2), (perimeter, 2)]