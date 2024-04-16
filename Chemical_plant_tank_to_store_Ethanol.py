''' Chemical plant has a tank for storing ethanol.
80% full raise an alarm to close the valve.
20% full send a SMS to buy more liquid
Total tank capacity is 900 liters '''

def do_action(present, redmark, bluemark):
    if present <= redmark:
        print(" Buy more liquid")
    elif present >= bluemark:
        print("Close the valve")
    else:
        print("No action required")

def get_current_level():
    level = int(input("Enter the current level of tank: "))
    return level

# main starts from here
capacity = 900
high = (900 * 80) // 100
low = (900 * 20) // 100
level = get_current_level()

do_action(level, high, low)
