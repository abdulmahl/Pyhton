b = ["banana", "apple", "macOs", 777, "nachos"]

# b[2] = "banana"
# b[0] = "macOs"
b.append("python")
b.append(99)
b.remove(777)
temp = b[0]
b[0] = b[2]
b[2] = temp

for item in b:
    print(item)