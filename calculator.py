def is_number(num):
    return num.replace('.', '', 1).isdigit()

def perform_operation(num_1, num_2, operation):
    if operation == 1:
        return num_1 + num_2
    elif operation == 2:
        return num_1 - num_2
    elif operation == 3:
        if num_2 == 0:
            return "Error: Division by zero"
        return num_1 / num_2
    elif operation == 4:
        return num_1 * num_2
    else:
        return "Invalid operation"

num_1 = input("Enter the first number:\n")
try:
    if not is_number(num_1):
        raise ValueError
    num_1 = float(num_1)
except ValueError:
    print("Invalid input")
    quit()

num_2 = input("Enter the second number:\n")
try:
    if not is_number(num_2):
        raise ValueError
    num_2 = float(num_2)
except ValueError:
    print("Invalid input")
    quit()

print("1. Addition\n"
      "2. Subtraction\n"
      "3. Division\n"
      "4. Multiplication")

try:
    operation = int(input("Enter the number corresponding to the operation you want to perform:\n"))
except ValueError:
    print("Invalid input")
    quit()

result = perform_operation(num_1, num_2, operation)

if isinstance(result, float):
    result = str(result).rstrip(".0")

print(f"The result is:\n{result}")
