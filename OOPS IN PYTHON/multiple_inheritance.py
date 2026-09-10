# multiple inheritance = inherit from more than one parent class
#                         C(A,B)

# multilevel inheritance=inherit from a parent which inherits from another parent
#                         C(B) <- B(A) <- A


class Animal:
    def eat(self):
        print("this animal is eating")
    def sleep(self):
        print("this animal is sleeping")

class Prey:
    def flee(self):
        print("this animal is fleeing ")

class Predator:
    def hunt(self):
        print("this animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

