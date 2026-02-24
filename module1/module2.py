try:
    # Taking input from the user
    # float() allows both integers and decimal numbers
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    # Performing calculations
    addition = first_number + second_number
    subtraction = first_number - second_number
    multiplication = first_number * second_number
    exponentiation = first_number ** second_number

    # Handling division and modulus separately
    if second_number != 0:
        division = first_number / second_number
        modulus = first_number % second_number
    else:
        division = "Undefined (Cannot divide by zero)"
        modulus = "Undefined (Cannot divide by zero)"

    # Displaying results
    print("\n----- CALCULATION RESULTS -----")
    print("Addition:", addition)
    print("Subtraction:", subtraction)
    print("Multiplication:", multiplication)
    print("Division:", division)
    print("Modulus:", modulus)
    print("Exponentiation:", exponentiation)

# This block runs if the user enters something that is not a number
except ValueError:
    print("Invalid input! Please enter numeric values only.")

# This block handles unexpected division by zero errors
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")

# This block handles any other unexpected errors
except Exception as error:
    print("Something went wrong:", error)
