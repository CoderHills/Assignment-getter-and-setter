ALL_COURSES = [
    "Data Science",
    "Software Engineering",
    "DevOPS",
    "Cyber Security",
    "AI Engineering",
    "High School Bootcamp",
    "Product Design",
    "Data Analytics",
    "Data Analytics for HR Professionals",
]


class Student:
    student_count = 0
    all_students = []

    def __init__(
        self, first_name, last_name, age, gender, student_id, course, instructor
    ):
        self.first_name = first_name
        self.last_name = last_name
        self._age = None
        self._gender = None
        self.age = age       
        self.gender = gender  
        self.student_id = student_id
        self.course = course
        self.instructor = instructor


        if self._age is not None:
            Student.student_count += 1
            Student.all_students.append(self)

    # getter for age
    @property
    def age(self):
        return self._age

    # setter for age
    @age.setter
    def age(self, value):
        if value < 18:
            print(f"{self.first_name} cannot enroll. Age must be 18 or above.")
            self._age = None
        else:
            self._age = value

    # getter for gender
    @property
    def gender(self):
        return self._gender

    # setter for gender
    @gender.setter
    def gender(self, value):
        if value.lower() not in ["male", "female"]:
            raise ValueError("Gender must be 'male' or 'female'")
        self._gender = value.lower()

    # Getter and setter for course
    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, course):
        if course in ALL_COURSES:
            self._course = course
        else:
            raise ValueError("The course listed is not offered")

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@student.moringaschool.com"

    @classmethod
    def total_students(cls):
        return f"The total number of students is: {cls.student_count}"

    @classmethod
    def student_list(cls):
        return [student.fullname for student in cls.all_students]

    @staticmethod
    def reverse_name(first_name, last_name):
        return f"{last_name} {first_name}"



student1 = Student(
    "Bradley", "Murimi", 40, "Male", "MSS-1234", "Software Engineering", "Fainus Mudahe"
)
student2 = Student(
    "Mariam",
    "Rashid",
    20,
    "Female",
    "MSS-1428",
    "Software Engineering",
    "Julius Mutindwa",
)
student3 = Student(
    "Fredrick",
    "Rangara",
    50,
    "Male",
    "MSS-1480",
    "Software Engineering",
    "Julius Mutindwa",
)
student4 = Student(
    "Adonis",
    "Pierre",
    16, 
    "Male",
    "MSS-3445",
    "Data Science",
    "Julius Mutindwa",
)

print("\nEnrolled Students:")
for s in Student.all_students:
    print(s.fullname, "", s.age, "", s.gender, "", s.course)

