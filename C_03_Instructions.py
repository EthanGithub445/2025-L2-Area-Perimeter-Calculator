def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")

def instructions():
    make_statement("Instructions", "ℹ️")
    print("This program helps you calculate the area and perimeter (or circumference)")
    print(" of different shapes. Pick a number from 1-4 to pick a shape and enter the measurements")
    print(" asked for such as side length, radius, base, height, etc. The program will then calculate")
    print(" and show the area and perimeter (or circumference). You can either choose to calculate")
    print(" another shape or finish and see all your results displayed in a table.")
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

want_instructions = string_check("Do you want to read the instructions? ")

if want_instructions == "yes":
    instructions()
