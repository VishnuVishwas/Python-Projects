# class.py

from student import Student
from department import Department
from faculty import Faculty
from class_room import ClassRoom

class Class:
    def __init__(self, class_teacher: str, students: list, class_room):
        self.class_id = class_room.class_id
        self.class_teacher = class_teacher
        self.students = students

    # display class info
    def display_class_info(self):
        print("\nClass info:")
        print(f"Class Teacher: {self.class_teacher}")
        print("Students:")
        for student in self.students:
            print(f" - {student.student_name}")

if __name__ == '__main__':

    student1 = Student('1', 'John', 'B', '9')
    student2 = Student('2', 'Alice', 'A', '10')

    faculty = Faculty('2', 'vishnu', '001', '10')
    faculty.display_faculty_info()

    department = Department(1, 'Gojo')
    department.display_department_info()

    room = ClassRoom('100', '500')
    room.display_class_room_info()

    # Passing a list of Student instances
    students = [student1, student2]
    class1 = Class('Anya', students, room)
    class1.display_class_info()
