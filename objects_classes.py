
class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print(f"""My name is {self.name}
I'm {self.color} in color, 
and I weigh {self.weight} kilograms. 
I'm a bot, nice to meet you""")



# r1 = Robot()
# r1.name = "Anubis"
# r1.color = "red"
# r1.weight = 45

# r2 = Robot()
# r2.name = "Horus"
# r2.color = "gold"
# r2.weight = 56

r1 = Robot("Anubis", "red", 45)
r2 = Robot("Horus", "scarlet", 66)

r1.introduce_self()

# r2.introduce_self()
