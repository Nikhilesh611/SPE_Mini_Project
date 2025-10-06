import math

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

def power(x, b):
    return x ** b


# Menu-driven CLI
def main():
    while True:
        print("\n--- Scientific Calculator ---")
        print("1. Square Root (√x)")
        print("2. Factorial (!x)")
        print("3. Natural Logarithm (ln(x))")
        print("4. Power (x^b)")
        print("5. Exit")

        choice = input("Select an operation (1-5): ")

        if choice == "1":
            try:
                x = float(input("Enter a number: "))
                print(f"√{x} = {square_root(x)}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            try:
                x = int(input("Enter an integer: "))
                print(f"{x}! = {factorial(x)}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            try:
                x = float(input("Enter a number: "))
                print(f"ln({x}) = {natural_log(x)}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            try:
                x = float(input("Enter the base (x): "))
                b = float(input("Enter the exponent (b): "))
                print(f"{x}^{b} = {power(x, b)}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select from 1-5.")


if __name__ == "__main__":
    main()
