num_1 = float(input("What is the first number?: "))
num_2 = float(input("What is the second number?: "))

print("1. Addition\n"
      "2. Subtraction\n"
      "3. Division\n"
      "4. Multiplication")
funct = int(input("What is the function you would like to use?: "))

if funct == 1:
    ans = str(float(num_1 + num_2))
    print(f"The answer is {ans}")
elif funct == 2:
    ans = str(float(num_1 - num_2))
    print(f"The answer is {ans}")
elif funct == 3:
    ans = str(float(num_1 / num_2))
    print(f"The answer is {ans}")
elif funct == 4:
    ans = str(float(num_1 * num_2))
    print(f"The answer is {ans}")