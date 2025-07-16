# Function to calculate for triangle
def calculate_triangle():
    a = float(input("Side a: "))
    b = float(input("Side b: "))
    c = float(input("Side c: "))
    height = float(input("Height: "))
    # Area using half base x height
    area = 0.5 * (b * height)

    # Perimeter by adding all sides (side b for base)
    perimeter = a + b + c
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")

    return ["Triangle", f"Sides={a}, {b}, {c}, Height={height}", (area, 2), (perimeter, 2)]
calculate_triangle()