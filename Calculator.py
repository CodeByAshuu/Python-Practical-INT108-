'''
Made By: SAGAR SAHU
@Twitter : Ashuuu_7
@LinkedIn : www.linkedin.com/in/sagarr7
'''


# Input from the user..
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Check if the second number is not zero to avoid division by zero error
if num2 != 0:
    division = num1 / num2
    integer_division = num1 // num2
    modulo = num1 % num2
else:
    division = "Undefined (division by zero)"
    integer_division = "Undefined (division by zero)"
    modulo = "Undefined (division by zero)"

# Print the results
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Integer Division: {integer_division}")
print(f"Modulo: {modulo}")
