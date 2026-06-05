# create a rectangle

rows = int(input("enter num of rows: "))
columns = int(input("enter num of columns: "))
symbols = input("enter symbol to use: ")


for x in range(rows):
    for y in range(columns):
        print(symbols, end = "")
    print()     