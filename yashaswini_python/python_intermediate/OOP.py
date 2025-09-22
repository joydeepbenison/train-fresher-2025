class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Inheritance
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def student_info(self):
        return f"{self.name} is in grade {self.grade}."

# Objects
p1 = Person("Alice", 20)
s1 = Student("Bob", 18, "A")

print(p1.greet())
print(s1.greet())
print(s1.student_info())

