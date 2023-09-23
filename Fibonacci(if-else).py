'''
Made By: SAGAR SAHU
@Twitter : Ashuuu_7
@LinkedIn : www.linkedin.com/in/sagarr7
'''
# Input from the user
n = int(input("Enter the number of terms in the Fibonacci series: "))

# Check if the number of terms is valid
if n <= 0:
    print("Please enter a positive integer for the number of terms.")
else:
    a, b = 0, 1
    print(f"Fibonacci series with {n} terms:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
