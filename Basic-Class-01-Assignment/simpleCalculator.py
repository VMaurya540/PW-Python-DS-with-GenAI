# Build a simple calculator using conditional statements and operators.

print("Simple Calculator")
print("1. Add")
print("2. Multiply")
print("3. Substract")
print("4. Division")

choice = int(input("Enter choice (1/2/3/4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result: ", num1 + num2)
    
elif choice ==2:
    print("Result: ", num1 * num2)

elif choice == 3:
    print("Result: ", num1 - num2)

elif choice == 4:
    if num2 != 0:
        print("Result: ", num1 / num2)
    else:
        print("Error: Can not divide by zero")

else:
    print("Invalid choice")

    
