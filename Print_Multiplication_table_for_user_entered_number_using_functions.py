''' Program to print the multiplication table for user entered number
using python functions '''

def multiplication_table():
    num = int(input("Enter a number for multiplication table: "))
    print("Below is the multiplication table for: ", num)
    i = 1
    while i <= 10:
        table = i * num
        print(table)
        i = i + 1
multiplication_table()
