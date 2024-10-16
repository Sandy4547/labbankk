from student import Student
from teacher import Teacher

university = [
    Teacher("Dr. Smith", 45, "drsmith@university.com", "T001"),
    Teacher("Prof. Johnson", 50, "johnson@university.com", "T002"),
    Teacher("Ms. Davis", 38, "davis@university.com", "T003"),
    Student("Alice", 20, "alice@student.com", "S001"),
    Student("Bob", 22, "bob@student.com", "S002"),
    Student("Charlie", 19, "charlie@student.com", "S003")
]

# Demonstrating polymorphism
for i, person in enumerate(university):
    print(i + 1, end=". ")
    person.display_info()
