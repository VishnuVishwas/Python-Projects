# Admission of student & faculty in department

from models.student import Student
from models.faculty import Faculty
from models.courses import Courses

class Department:

    department_list = {'CSE', 'ECE', 'Mech', 'Civil', 'Robotics'}

    def __init__(self, department_name: str):
        self.department_name = department_name
        self.students = []
        self.faculty = []
        self.courses = []

    def admit_student(self, student_id: str, student_name: str):
        student = Student(student_id, student_name)
        self.students.append(student)
        print(f"Student '{student.student_name}' admitted to department {self.department_name}")

    def admit_faculty(self, faculty_id: str, faculty_name: str):
        faculty = Faculty(faculty_id, faculty_name)
        self.faculty.append(faculty)
        print(f"Faculty '{faculty.faculty_name}' admitted to department {self.department_name}")

    def create_course(self, course_id: str, course_name: str):
        course = Courses(course_id, course_name)
        self.courses.append(course)
        print(f"Course '{course.course_name}' created in '{self.department_name}' Department")

    def update_student_details(self, student_id: str, new_name: str):
        for student in self.students:
            if student.roll_no == student_id:
                student.student_name = new_name
                print(f"Student '{student.student_name}' updated")

    def update_faculty_details(self, faculty_id: str, new_name: str):
        for faculty in self.faculty:
            if faculty.faculty_id == faculty_id:
                faculty.faculty_name = new_name
                print(f"Faculty '{faculty.faculty_name}' updated")

    def delete_student(self, student_id: str):
        for student in self.students:
            if student.roll_no == student_id:
                self.students.remove(student)
                print(f"Student '{student.student_name}' deleted from {self.department_name} Department")
                break
        else:
            print(f"Student with ID {student_id} was not found.")

    def delete_faculty(self, faculty_id: str):
        for faculty in self.faculty:
            if faculty.faculty_id == faculty_id:
                self.faculty.remove(faculty)
                print(f"Faculty '{faculty.faculty_name}' deleted from '{self.department_name}'")
                break
        else:
            print(f"Faculty with ID {faculty_id} was not found. ")
