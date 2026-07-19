# #Inheritance = Allows a class to inherit attributes and methods from another class
#                 Helps with code reusability and extensibility
#                 class child(parent)

class Animal:
    def __init__(self, name):
        self.name=name
        self.is_alive=True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOOF")

class Cat(Animal):
    def speak(self):
        print("MEOWW")

class Mouse(Animal):
    def speak(self):
        print("SQUEAKKK")

dog=Dog("Scooby")
cat=Cat("Garfield")
mouse=Mouse("Jerry")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()  
dog.speak()