# Definig functions:
# Adding two numbers
def add(a, b):
    return a + b

# Subtracting two numbers
def subtract(a, b):
    return a - b

# Multipling two numbers
def multiply(a, b):
    return a * b

# Dividing two numbers
def divide(a, b):
    return a / b


print("Choose an operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # input from the user
    choice = input("choose a number between 1 an 4: ")

    # checking whether the choice exisits 
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("first number: "))
            num2 = float(input("second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop otherwise
        next_calculation = input("Would you like to calculate something else? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
