# student.py

class Student:
    def __init__(self, student_id: str, student_name: str, section: str, grade: str):
        self.student_id = student_id
        self.student_name = student_name
        self.section = section
        self.grade = grade

    # detials of student
    def display_student_info(self):
        print(f"\nStudent details:\nStudent ID: {self.student_id}\nName: {self.student_name}\nSection: {self.section}\nGrade: {self.grade}")

if __name__ == "__main__":
    student = Student('2', 'vishnu', 'A', '10')
    student.student_info()
        