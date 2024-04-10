''' Program to print the multiplication table for user Entered Number'''

def get_number():
    number = int(input("Enter a number to print multiplication table: "))
    return number
def print_mtable(num):
        i = 1
        while i <= 10:
            a = i * num
            i+= 1
            print(a)
def main():
    inp = get_number()
    print_mtable(inp)

main()
