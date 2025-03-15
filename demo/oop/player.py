class Player:
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def __str__(self):
        return  f"{self.name} - {self.game}"

    def __eq__(self, other):
        print("__eq__")
        return self.name == other.name and self.game == other.game

    def __gt__(self, other):
        return self.name > other.name

p1 = Player("Dhoni", "Cricket")
p2 = Player("Ronaldo", "Football")
p3 = Player("Dhoni", "Cricket")

print(p1)
print(str(p1))
print(p1.__str__())
print(p1 == p3)       # Compare addresses
print(p1.__eq__(p3))  # Compare contents
print(p1 != p2)       # Compare contents
print(p1  > p2, p2 > p3)








