# Function to calculate for square
def calculate_square():
    side = int(input("side length: "))
    # Area using length squared
    area = side ** 2
    # Perimeter using 4 x side
    perimeter = 4 * side
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
    return ["Square", f"Side={side}", area, perimeter]

calculate_square()

