# Excercise 5 - More Variable and Printing

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_in_centimeter = height * 2.54 # because 1 Inch = 2.54 Centimeter
weight_in_kilogram = weight * 0.453292 # 1 pound = 0.453592 Kilogram

print(f"Lets talk about {name}.")
print(f"He's {height} inches or {round(height_in_centimeter)} tall.")
print(f"He's {weight} pounds heavy and {round(weight_in_kilogram)} in kilogram .")
print("Actually thats not too heavy.")
print(f"He's got {eyes} and {hair} hair.")
print(f"His teeth are usally {teeth} depending on the coffee.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
