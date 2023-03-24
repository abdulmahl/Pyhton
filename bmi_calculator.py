name1 =  str(input("Enter your name: ")).title()
height_m1 = float(input("Enter your height in (meters): "))
weight_kg1 = int(input("Enter your weight in (Kilograms): "))
print()

name2 = str(input("Enter your name: ")).title()
height_m2 = float(input("Enter your height in (meters): "))
weight_kg2 = int(input("Enter your weight in (Kilograms): "))
print()

name3 = str(input("Enter your name: ")).title()
height_m3 = float(input("Enter your height in (meters): "))
weight_kg3 = int(input("Enter your weight in (Kilograms): "))

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / height_m **2
    if bmi < 25:
        return (f"{name}, with bmi {bmi:.1f}, is not overweight")
    else:
        return (f"{name}, with bmi of {bmi:.1f}, is overweight")

results1 = bmi_calculator(name1, height_m1, weight_kg1)
results2 = bmi_calculator(name2, height_m2, weight_kg2)
results3 = bmi_calculator(name3, height_m3, weight_kg3)

print(results1)
print(results2)
print(results3)
