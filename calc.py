from InquirerPy import inquirer
import math

def square_root():
    x = float(input("Enter a number: "))
    if x < 0:
        print("Error: Cannot calculate square root of a negative number.")
    else:
        print(f"√{x} = {math.sqrt(x)}")

def factorial():
    x = int(input("Enter an integer: "))
    if x < 0:
        print("Error: Factorial not defined for negative numbers.")
    else:
        print(f"{x}! = {math.factorial(x)}")

def natural_log():
    x = float(input("Enter a number: "))
    if x <= 0:
        print("Error: ln(x) is only defined for x > 0.")
    else:
        print(f"ln({x}) = {math.log(x)}")

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
            square_root()
        elif choice == "Factorial (!x)":
            factorial()
        elif choice == "Natural Logarithm (ln(x))":
            natural_log()
        elif choice == "Exit":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
