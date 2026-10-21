
class Bird:
    def __init__(self, name, color, weight):
        self.__name = name
        self.__color = color
        self.__weight = weight

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    @property
    def weight(self):
        return self.__weight

    def describe(self):
        return (
            f"Name: {self.name}, "
            f"Color: {self.color}, "
            f"Weight: {self.weight} kg"
        )


class Eagle(Bird):
    def fly(self):
        return f"{self.name} can fly."


class Penguin(Bird):
    def swim(self):
        return f"{self.name} can swim."

    def walk(self):
        return f"{self.name} can walk."


class Ostrich(Bird):
    def run(self):
        return f"{self.name} can run."

    def walk(self):
        return f"{self.name} can walk."


eagle = Eagle("Eagle", "Brown", 5)
penguin = Penguin("Penguin", "Black and white", 15)
ostrich = Ostrich("Ostrich", "Brown", 100)

print("=== Bird Information ===")
print(eagle.describe())
print(penguin.describe())
print(ostrich.describe())

print("\n=== Bird Behaviors ===")
print(eagle.fly())
print(penguin.swim())
print(penguin.walk())
print(ostrich.run())
print(ostrich.walk())

# Verify that unsuitable behavior is not inherited
print("\n=== Capability Checks ===")
print("Eagle can fly:", hasattr(eagle, "fly"))
print("Penguin can fly:", hasattr(penguin, "fly"))
print("Ostrich can fly:", hasattr(ostrich, "fly"))
