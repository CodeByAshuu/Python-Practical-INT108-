'''
Made By: SAGAR SAHU
@Twitter : Ashuuu_7
@LinkedIn : www.linkedin.com/in/sagarr7
'''
def is_palindrome(input_string):
    # Remove spaces and convert the string to lowercase for accurate comparison
    cleaned_string = input_string.replace(" ", "").lower()
    
    # Initialize pointers for the start and end of the string
    start = 0
    end = len(cleaned_string) - 1

    # Check if the string is a palindrome using a loop
    while start < end:
        if cleaned_string[start] != cleaned_string[end]:
            return False
        start += 1
        end -= 1

    return True

# Input a string from the user
user_input = input("Enter a string: ")

# Check if it's a palindrome and print the result
if is_palindrome(user_input):
    print("The entered string is a palindrome.")
else:
    print("The entered string is not a palindrome.")
