import math
import pandas

# Functions go here
def num_check(question, num_type, exit_code=None):
    """Checks that the user enters an integer / float that is more than
    zero (or the optional exit code)"""

    if num_type == "integer":
        error = "oops - please enter an integer more than zero"
        change_to = int
    else:
        error = "oops - please enter an integer more than zero"
        change_to = float

    while True:
        response = input(question).lower()

        # check for the exit code
        if response == exit_code:
            return response

        try:
            # Change the response to an integer and check that it's more than zero
            response = change_to(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

def instructions():
    make_statement("Instructions", "ℹ️")
    print(" This program helps you calculate the area and perimeter (or circumference)")
    print(" of different shapes. Pick a number from 1-4 to pick a shape and enter the measurements")
    print(" asked for such as side length, radius, base, height, etc. The program will then calculate")
    print(" and show the Results. You can either choose to calculate")
    print(" another shape or finish and see all your results displayed in a table.")
    print(" In order to calculate a triangle you must have all 3 sides and the height.")
    print(" Make sure to only enter numbers when asked for measurements and enjoy calculating.")


def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    """Checks that users enter the full word or the 'n' letter/s
    of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # Check if the response is the entire word
            if response == item:
                return item
            # check if it's the 'n' letters
            elif response == item[:num_letters]:
                return item
        print(f"please choose an option from {valid_answers}")


def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")

# Calculate area and perimeter for a square


def calculate_square():
    side = num_check("Enter the side length of the square: ", "integer")
    area = side * side
    perimeter = 4 * side
    return ["Square", f"Side = {side}", area, perimeter]


# Calculate area and perimeter for a rectangle
def calculate_rectangle():
    length = num_check("Length: ", "integer")
    width = num_check("Width: ", "integer")
    area = length * width
    perimeter = 2 * (length + width)
    return ["Rectangle", f"Length = {length}, Width = {width}", area, perimeter]


# Calculate area and circumference for a circle
def calculate_circle():
    radius = num_check("Enter the radius of the circle: ", "float")
    area = math.pi * radius * radius
    perimeter = 2 * math.pi * radius
    return ["Circle", f"Radius = {radius}", round(area, 2), round(perimeter, 2)]


# Calculate area (using base and height) and perimeter (sum of sides) for a triangle
# Here we use side b as the base for the area calculation
def calculate_triangle():
    a = num_check("Side A: ", "integer")
    b = num_check("side B (This will be the base): ", "integer")
    c = num_check("Side C: ", "integer")
    height = num_check("Height: ", "integer")
    area = 0.5 * b * height
    perimeter = a + b + c
    return ["Triangle", f"a = {a}, b = {b}, c = {c}, height = {height}", round(area, 2), round(perimeter, 2)]

# Main routine


make_statement("Area Perimeter Calculator", "✨")
print()
want_instructions = string_check("Do you want to read the instructions? ")
print()

if want_instructions == "yes":
    instructions()
print()
# Create an empty list to store the results
results = []

while True:
    # Ask user to pick a shape and show options
    print("Choose a shape to calculate its area and perimeter:")
    print("1 - Square")
    print("2 - Rectangle")
    print("3 - Circle")
    print("4 - Triangle")

    choice = input("Pick a shape 1-4: ")
    # Depending on which shape is picked, a different function is used and results are added to result list
    if choice == "1":
        results.append(calculate_square())
    elif choice == "2":
        results.append(calculate_rectangle())
    elif choice == "3":
        results.append(calculate_circle())
    elif choice == "4":
        results.append(calculate_triangle())

    else:
        # If number between 1 - 4 is not selected, ask again
        print("Please choose a number between 1 and 4")
        continue

    # Ask user if they want to calculate another shape, if not display results
    another = string_check("Do you want to calculate another shape? (yes/no): ")
    if another == "no":
        break

# Display all the calculations in a table using pandas
if results:
    data = pandas.DataFrame(results, columns=["Shape", "Dimensions", "Area", "Perimeter"])
    make_statement("Area and Perimeter Calculations:", "✨")
    print(data)
