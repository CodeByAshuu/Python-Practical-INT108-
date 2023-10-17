'''
Made By: SAGAR SAHU
@Twitter : Ashuuu_7
@LinkedIn : www.linkedin.com/in/sagarr7

'''

#-----Pyramid---------
n=int(input("n: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("# ",end="")
    print()                     

# -------Floyyd Pyramid-----
n=int(input("Enter: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#Pascal's Triangle
num_rows = int(input("Enter the number of rows for Pascal's Triangle: "))
current_row = [1]

for i in range(num_rows):
    for j in range(num_rows - i - 1):
        print(" ", end="")
    
    for j in range(len(current_row)):
        print(current_row[j], end=" ")
    
    next_row = []
    for j in range(len(current_row) - 1):
        next_row.append(current_row[j] + current_row[j + 1])
    
    next_row = [1] + next_row + [1]
    
    current_row = next_row
    print()