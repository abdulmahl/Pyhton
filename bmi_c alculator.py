name1 = "YK"
height_m1 = 2
weight_kg1 = 90

name2 = "YK's sister"
height_m2 = 1.8
weight_kg2 = 70

name3 = "YK's brother"
height_m3 = 2.5
weight_kg3 = 160

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / height_m **2
    # print(f"bmi: {bmi:.1f}")
    if bmi < 25:
        return (f"{name}, with bmi {bmi:.1f}, is not overweight")
    else:
        return (f"{name},e with bmi of {bmi:.1f}, is overweight")

results1 = bmi_calculator(name1, height_m1, weight_kg1)
results2 = bmi_calculator(name2, height_m2, weight_kg2)
results3 = bmi_calculator(name3, height_m3, weight_kg3)

print(results1)
print(results2)
print(results3)
