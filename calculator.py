# calculator.py

def calculator(num1, num2, operation):
    """
    Performs arithmetic operations on two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform. Can be 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
        float: The result of the operation.

    Raises:
        ValueError: If the operation is not one of 'add', 'subtract', 'multiply', or 'divide'.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero")
    else:
        raise ValueError("Invalid operation")

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operation_input(prompt):
    while True:
        operation = input(prompt).lower()
        if operation in ['+', '-', '*', '/']:
            return operation
        else:
            print("Invalid operation. Please use one of the following: +, -, *, /")

def main():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = get_float_input("Enter the first number: ")
        num2 = get_float_input("Enter the second number: ")

        if choice == '1':
            operation = 'add'
        elif choice == '2':
            operation = 'subtract'
        elif choice == '3':
            operation = 'multiply'
        elif choice == '4':
            operation = 'divide'

        try:
            result = calculator(num1, num2, operation)
            print(f"{num1} {operation} {num2} = {result}")
        except ValueError as e:
            print(e)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()