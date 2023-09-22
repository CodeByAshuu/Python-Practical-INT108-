'''
Made By: SAGAR SAHU
@Twitter : Ashuuu_7
@LinkedIn : www.linkedin.com/in/sagarr7
'''
# Input from the user
user_input = input("Enter a string: ")

# Remove spaces and convert to lowercase
input_string = user_input.replace(" ", "").lower()

# Initialize pointers
left = 0
right = len(input_string) - 1

# Check if it's a palindrome
is_palindrome = True

while left < right:
    if input_string[left] != input_string[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
