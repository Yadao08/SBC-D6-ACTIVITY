rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

if rows <= 0 or columns <= 0:
    print()
else:
    current_row = 0
    while current_row < rows:
        current_column = 0
        while current_column < columns:
            if current_row in [0, rows - 1] or current_column in [0, columns - 1]:
                print("*", end="")
            else:
                print(" ", end="")
            current_column += 1
        print()
        current_row += 1
