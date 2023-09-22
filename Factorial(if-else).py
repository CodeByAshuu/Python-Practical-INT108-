'''
Made By: SAGAR SAHU
@Twitter : Ashuuu_7
@LinkedIn : www.linkedin.com/in/sagarr7

'''
# Input from the user
num = int(input("Enter a number: "))

# Initialize the result
factorial = 1

# Calculate the factorial using a loop
for i in range(1, num + 1):
    factorial *= i

# Print the factorial
print(f"The factorial of {num} is {factorial}")
