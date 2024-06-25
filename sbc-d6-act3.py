#diamond shape
num_of_rows = int(input("Enter the number of rows: "))

for i in range(num_of_rows, 1, -1):     #descending pattern
    print('*' * i)

if num_of_rows > 1:     # asterisks
    print('*' + ' ' * (num_of_rows - 3) + '*')

for i in range(2, num_of_rows + 1): #ascending
    print('*' * i)
