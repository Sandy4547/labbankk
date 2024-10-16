from person import Person

class Student(Person):
    def __init__(self, name, age, email, student_id):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)

    def display_courses(self):
        print(f"{self.name} is enrolled in the following courses: {', '.join(self.courses)}")

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        if self.courses:
            self.display_courses()
        print("----------")

    def update_email(self, new_email):
        self.email = new_email
        print(f"{self.name}'s email has been updated to: {self.email}")
