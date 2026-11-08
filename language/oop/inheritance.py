class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

# class JackRussellTerrier(Dog):
    # def speak(self, sound="Arf"):
    #     return super().speak(sound)
    
# class Dachshund(Dog):
#     pass
# class Bulldog(Dog):
#     pass


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


mew = GoldenRetriever("Meww", 20)

# print(mew.speak())

# miles = JackRussellTerrier("Jack", 30)
# mew = Dachshund("Mew", 40)


# print(isinstance(miles, ( JackRussellTerrier)))

# print(miles.speak())

# print(mew.speak("Mewwwwww"))
# class Car:
#     def __init__(self, color, mileage):
#         self.color = color
#         self.mileage = mileage
#     def __str__(self):
#         return f"The {self.color} car has {self.mileage:,} miles"



# blue_car = Car(color="blue", mileage=20_000)
# red_car = Car(color="red", mileage=30_000)

# print(blue_car)


class Parent:
    speaks = ["English"]

    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name):
        super().__init__(name)
        self.speaks = Parent.speaks + ["German"]




obj =  Child('ola')
print(obj.name)
print(obj.speaks)


