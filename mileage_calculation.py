'''
 Program to calculate the cars milage
 
'''
start_value = int(input("Enter start value of Odometer: "))
End_value = int(input("Enter the end value of odometer: "))
Enter_fuel_filled_in_ltr = int(input("Enter number of liters fuel filled: "))
Total_km_travelled = End_value - start_value
car_mileage = Total_km_travelled / Enter_fuel_filled_in_ltr
print(car_mileage)
