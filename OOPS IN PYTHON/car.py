class Car:
    def __init__(self, model, year, color, for_sale): #dunder method= double underscore..init means to initialaise
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale

    #methods
    def drive(self):
        print("you drive the car")
    
    def stop(self):
        print("you stop the car")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")