# Program to calculate BMI

# take input from the user
height_in_inches = float(input("Input your height in inches: "))
weight_in_kg = float(input("Input your weight in kg: "))

# Convert height in meter
height_in_meter = (height_in_inches / 39.37)

# calculate BMI
bmi = weight_in_kg / (height_in_meter ** 2)

# print the BMI
print("Your BMI is:", round(bmi, 2))

# calculate min expected weight in kg
expected_weight_min = (height_in_meter ** 2) * 18.5

# calculate min expected weight in kg
expected_weight_max = (height_in_meter ** 2) * 24.9

# print the expected weight
print("Your minimum expected weight in kg is:", int(expected_weight_min))

# print the expected weight
print("Your weight should not exceed:", int(expected_weight_max))
