import math
# Function to calculate for circle
def calculate_circle():
    radius = float(input("Radius: "))
    # Area using pi x radius squared
    area = math.pi * radius ** 2
    # Perimeter using 2 x pi x radius
    perimeter = 2 * math.pi * radius
    print(f"Area: {area:.3f}")
    print(f"Perimeter: {perimeter:.3f}")
    return ["Circle", f"Radius={radius}", (area, 2), (perimeter, 2)]

calculate_circle()