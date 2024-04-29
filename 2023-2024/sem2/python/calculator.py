def add(x, y):
    """Function to perform addition."""
    return x + y

def subtract(x, y):
    """Function to perform subtraction."""
    return x - y

def multiply(x, y):
    """Function to perform multiplication."""
    return x * y

def divide(x, y):
    """Function to perform division."""
    if y == 0:
        return "Error! Division by zero."
    return x / y

def perform_operation(x, y, operation):
    """Function to perform the selected operation."""
    if operation == '+':
        return add(x, y)
    elif operation == '-':
        return subtract(x, y)
    elif operation == '*':
        return multiply(x, y)
    elif operation == '/':
        return divide(x, y)
    else:
        return "Invalid operation!"

def calculator():
    """Function to execute the calculator program."""
    while True:
        print("\nOperations available:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                operation = '+' if choice == '1' else '-' if choice == '2' else '*' if choice == '3' else '/'
                result = perform_operation(num1, num2, operation)
                print("Equals:", result)
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        elif choice == '5':
            print("Exiting calculator. Thank you!")
            break
        else:
            print("Invalid choice! Please enter a valid option (1/2/3/4/5).")

if __name__ == "__main__":
    calculator()
