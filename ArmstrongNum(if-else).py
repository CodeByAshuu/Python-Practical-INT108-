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
2^4+6^4+9^4+8^4 = 2648     #4 digits so power to 4
"""

#Take input from user
num=input("Enter the Number: ")
print(num)

#Check length of number (number of digits)
r=len(num)
n=int(num)

#Setting sum  to zero
s=0
temp = n

#Check Armstrong or not
while temp>0:
    d=temp%10
    s+=d**r
    temp=temp//10
if s==n:
    print(n,"is a Armstrong number")
else:
    print(n,"is not a armstrong")