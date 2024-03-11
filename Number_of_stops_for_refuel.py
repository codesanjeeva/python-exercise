''' Program to calculate number of stops for refuel
while travelling 560km from bengalore to Goa '''

car_milage_per_ltr = int(input("Enter car milage per liter: "))
Tank_capacity_in_ltrs = int(input("Enter tank capacity in ltrs: "))
total_distance_in_km = 560
number_of_stops_for_refuel = 560 / (car_milage_per_ltr * Tank_capacity_in_ltrs)
print("number of stops for refuel = ", number_of_stops_for_refuel)
