#class variables = shared among all instances of a class
#                  defined outside the constructor
#                  allow you to share data among all objects created from that class

class Student:

    class_year=2024  #class_year is the class variable as we can directly access it from the class
    num_students=0

    def __init__(self, name, age): #self refers to the object we are currently working with
        self.name=name
        self.age=age
        Student.num_students+=1

student1 = Student("Rajshree", 22)
student2=Student("Mouley", 20)
student3=Student("Aashi", 22)

print(student1.name)
print(student1.age)
print(Student.class_year)  #good to access class variable by the class name itself and not the instance of the class

print(Student.num_students)
print(f"my graduating class of {Student.class_year} has {Student.num_students} students") 
