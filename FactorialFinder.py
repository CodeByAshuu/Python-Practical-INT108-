'''
Made By: SAGAR SAHU
@Twitter : Ashuuu_7
@LinkedIn : www.linkedin.com/in/sagarr7

'''
# Function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Input from the user
num_str = input("Enter a number: ")

# Check if the input is a valid integer
if num_str.isdigit():
    num = int(num_str)
    
    # Check if the number is non-negative (factorial is not defined fro negative no. LOL!)
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(num)
        print(f"The factorial of {num} is {result}")
else:
    print("Invalid input. Please enter a valid number.")
