class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Email: {self.email}")

    def update_email(self, new_email):
        self.email = new_email
        print(f"{self.name}'s email has been updated to: {self.email}")

class Student(Person):
    def __init__(self, name, age, email, student_id):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.courses = []

    def enroll_course(self, course_name):
        self.courses.append(course_name)
        print(f"{self.name} has enrolled in the course: {course_name}")

    def display_courses(self):
        if self.courses:
            print(f"{self.name} is enrolled in the following courses: {', '.join(self.courses)}")
        else:
            print(f"{self.name} has not enrolled in any courses yet.")

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        self.display_courses()

student1 = Student("Alex Smith", 20, "alexsmith@example.com", "S123456")
student1.display_info()
student1.enroll_course("Mathematics")
student1.enroll_course("Physics")
student1.display_courses()
student1.update_email("alex.smith@university.com")
print()
student1.display_info()