import math
from InquirerPy import inquirer

# Core functions
def square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    return math.factorial(x)

def natural_log(x):
    if x <= 0:
        raise ValueError("ln(x) is only defined for x > 0.")
    return math.log(x)


# CLI wrapper
def main():
    while True:
        choice = inquirer.select(
            message="Choose an operation:",
            choices=[
                "Square Root (√x)",
                "Factorial (!x)",
                "Natural Logarithm (ln(x))",
                "Exit"
            ],
        ).execute()

        if choice == "Square Root (√x)":
            x = float(input("Enter a number: "))
            try:
                print(f"√{x} = {square_root(x)}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "Factorial (!x)":
            x = int(input("Enter an integer: "))
            try:
                print(f"{x}! = {factorial(x)}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "Natural Logarithm (ln(x))":
            x = float(input("Enter a number: "))
            try:
                print(f"ln({x}) = {natural_log(x)}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "Exit":
            print("Exiting...")
            break
