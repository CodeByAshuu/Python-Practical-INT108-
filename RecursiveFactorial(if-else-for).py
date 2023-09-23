'''
Made By: SAGAR SAHU
@Twitter : Ashuuu_7
@LinkedIn : www.linkedin.com/in/sagarr7

'''
# Input from the user
num = int(input("Enter a natural number: "))

# Check if the number is non-negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")
