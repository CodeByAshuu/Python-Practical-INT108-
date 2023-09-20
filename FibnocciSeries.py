'''
Made By: SAGAR SAHU
@Twitter : Ashuuu_7
@LinkedIn : www.linkedin.com/in/sagarr7
'''

# Function to generate Fibonacci series
def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    
    return fib_series

# Input from the user
n = int(input("Enter the number of terms in the Fibonacci series: "))

# Check if the number of terms is valid
if n <= 0:
    print("Please enter a positive integer for the number of terms.")
else:
    # Generate and print the Fibonacci series
    result = fibonacci_series(n)
    print(f"Fibonacci series with {n} terms:")
    print(*result, sep=" ")
