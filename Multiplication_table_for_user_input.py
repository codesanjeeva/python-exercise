''' Program to print multiplication table for
user entered valid natural number'''

n = int(input("Enter a number for multiplication table: "))
multiplication_table = 0
i = 1
while i <=10:
    multiplication_table = n * i
    print(multiplication_table)
    i+=1
