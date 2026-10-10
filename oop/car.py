class Car:

    wheels =  4
    num_cars =  0

    def __init__(self, model, year, color, for_sale):
        self.model =  model
        self.year =  year
        self.color =  color
        self.for_sale =  for_sale
        Car.num_cars += 1
    

    def move(self):
        print(f"{self.model} can move")

    def stop(self):
        print(f"{self.model} can move")


    def __str__(self):
        return f"{self.color.capitalize()} {self.model} produce in {self.year} is {'for sale' if self.for_sale else 'not for sale'}" 


