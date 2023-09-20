'''
Made By: SAGAR SAHU
@Twitter : Ashuuu_7
@LinkedIn : www.linkedin.com/in/sagarr7

'''
"""ARMSTRONG NUMBER : A number is thought of as an Armstrong number if the 
sum of its own digits raised to the power number of digits gives the number itself.
For example:
1^1=1                      #1 digit so power to 1
1^3 + 5^3 + 3^3 = 153      #3 digits so power to 3
2^4+6^4+9^4+8^4 = 2468     #4 digits so power to 4
"""

# Function to check if a number is Armstrong
def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate the sum of digits raised to the power of the number of digits using a list comprehension
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    return sum_of_powers == number

# Input from the user
num_str = input("Enter a number: ")

# Check if the input is a valid integer
if num_str.isdigit():
    num = int(num_str)
    
    # Check if the number is Armstrong
    if is_armstrong_number(num):
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")
else:
    print("Invalid input. Please enter a valid number.")

#Write code here