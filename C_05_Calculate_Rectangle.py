# Function to calculate for rectangle
def calculate_rectangle():
    length = int(input("length: "))
    width = int(input("width: "))
    # Area using length x width
    area = length * width
    # Perimeter using 2 x (length + width)
    perimeter = 2 * (length + width)
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
    return ["Rectangle", f"Length={length}, Width={width}", area, perimeter]

calculate_rectangle()