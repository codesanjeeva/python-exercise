''' Program to print the multiplication table for given Number'''

def mlt(num):
    print("Printing Multiplication table for: ", num)
    i = 1
    while i <= 10:
        a = i * num
        i+= 1
        print(a)
# Main starts from here      
mlt(17)
mlt(20)


