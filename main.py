# inputs as strings
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#convert strings into integer and float
weight_new = int(weight)
height_new = float(height)

# Formula
# Using the exponent operator **
bmi = weight_new / height_new ** 2

bmi_as_int = int(bmi)

print(bmi_as_int)

