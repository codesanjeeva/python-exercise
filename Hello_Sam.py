""" This program will ask user to enter the name and Say hello to the user"""

def get_username():
    name = input("Enter your name: ")
    return name
    
def say_hello(name):
    print("Hello", name, "!!!")

def main():
    name = get_username()
    say_hello(name)

main()


