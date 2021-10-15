# Excercise 4 - variable and Names
# Here is a variable name cars which stote the total number of cars
cars = 100
# Space in every car
space_in_a_car= 4.0
# Total number of drivers
drivers = 30
# Total number of passengers
passengers = 90
# Number of cars not driven because of driver not available
cars_not_driven = cars - drivers
# Total number of cars driven by drivers
cars_driven = drivers
# Total capacity
carpool_capacity= cars_driven* space_in_a_car
# How many passenger can be transport in every car
average_passenger_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers_available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have",passengers, "to carpool today.")
print("We need to put about", average_passenger_per_car,"in each car.")
