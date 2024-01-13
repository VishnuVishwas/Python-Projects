# Addmission of student & faculty in department

from models.student import Student
from models.faculty import Faculty
from models.courses import Courses

# Department
class Department():
    def __init__(self, department_name: str):
        self.department_name = department_name
        self.students = []
        self.faculty = []
        self.courses = []

    def admit_student(self, student_name: str, roll_no: str):
        student = Student(student_name, roll_no)
        self.students.append(student)
        print(f"Student '{student.student_name}' admiited to '{self.department_name}' Department")

    def admit_faculty(self, faculty_id: str, faculty_name: str):
        faculty = Faculty(faculty_id, faculty_name)
        self.faculty.append(faculty)
        print(f"Faculty '{faculty.faculty_name}' addmitted to '{self.department_name}' Department")

    def create_course(self, course_id: str, course_name: str):       
        course = Courses(course_id, course_name)
        self.courses.append(course)
        print(f"Course '{course.course_name}' created in' {self.department_name}' Department")

    def update_student_details(self, student_id: str, new_name: str):   
        for student in self.students:
            if student.student_id == student_id:
                student.student_name = new_name