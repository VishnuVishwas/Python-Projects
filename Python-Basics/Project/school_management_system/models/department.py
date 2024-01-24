import csv

class Student:
    def __init__(self, roll_no: str, student_name: str) -> None:
        self.roll_no = roll_no
        self.student_name = student_name

    def __str__(self):
        return f"Student rollno: {self.roll_no}\nName: {self.student_name}"

class Faculty:
    def __init__(self, faculty_id: str, faculty_name: str) -> None:
        self.faculty_id = faculty_id
        self.faculty_name = faculty_name

    def __str__(self):
        return f"Faculty ID: {self.faculty_id}\nName: {self.faculty_name}"

class Courses:
    def __init__(self, course_id: str, course_name: str) -> None:
        self.course_id = course_id
        self.course_name = course_name

    def __str__(self) -> str:
        return f"Course ID: {self.course_id}\nCourse Name: {self.course_name}"

class Department:

    department_list = {'CSE', 'ECE'}

    def __init__(self, department_name: str):
        if department_name not in Department.department_list:
            raise ValueError(f"Invalid department name. Choose from {Department.department_list}")

        self.department_name = department_name
        self.students = []
        self.faculty = []
        self.courses = []
        self.file_name_student = f'{self.department_name}_students.csv'
        self.file_name_faculty = f'{self.department_name}_faculty.csv'
        self.file_name_courses = f'{self.department_name}_courses.csv'
        self.load_data_from_csv()

    def load_data_from_csv(self):
        try:
            with open(self.file_name_student, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    self.students.append(Student(row[0], row[1]))
        except FileNotFoundError:
            pass

        try:
            with open(self.file_name_faculty, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    self.faculty.append(Faculty(row[0], row[1]))
        except FileNotFoundError:
            pass

        try:
            with open(self.file_name_courses, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    self.courses.append(Courses(row[0], row[1]))
        except FileNotFoundError:
            pass

    def save_data_to_csv(self):
        with open(self.file_name_student, 'w', newline='') as file:
            writer = csv.writer(file)
            for student in self.students:
                writer.writerow([student.roll_no, student.student_name])

        with open(self.file_name_faculty, 'w', newline='') as file:
            writer = csv.writer(file)
            for faculty in self.faculty:
                writer.writerow([faculty.faculty_id, faculty.faculty_name])

        with open(self.file_name_courses, 'w', newline='') as file:
            writer = csv.writer(file)
            for course in self.courses:
                writer.writerow([course.course_id, course.course_name])

    def admit_student(self, student_id: str, student_name: str):
        student = Student(student_id, student_name)
        self.students.append(student)
        print(f"Student '{student.student_name}' admitted to department {self.department_name}")
        self.save_data_to_csv()

    def admit_faculty(self, faculty_id: str, faculty_name: str):
        faculty = Faculty(faculty_id, faculty_name)
        self.faculty.append(faculty)
        print(f"Faculty '{faculty.faculty_name}' admitted to department {self.department_name}")
        self.save_data_to_csv()

    def create_course(self, course_id: str, course_name: str):
        course = Courses(course_id, course_name)
        self.courses.append(course)
        print(f"Course '{course.course_name}' created in '{self.department_name}' Department")
        self.save_data_to_csv()

    def update_student_details(self, student_id: str, new_name: str):
        for student in self.students:
            if student.roll_no == student_id:
                student.student_name = new_name
                print(f"Student '{student.student_name}' updated")
                self.save_data_to_csv()
                break
        else:
            print(f"Student with ID {student_id} was not found.")

    def update_faculty_details(self, faculty_id: str, new_name: str):
        for faculty in self.faculty:
            if faculty.faculty_id == faculty_id:
                faculty.faculty_name = new_name
                print(f"Faculty '{faculty.faculty_name}' updated")
                self.save_data_to_csv()
                break
        else:
            print(f"Faculty with ID {faculty_id} was not found.")

    def delete_student(self, student_id: str):
        for student in self.students:
            if student.roll_no == student_id:
                self.students.remove(student)
                print(f"Student '{student.student_name}' deleted from {self.department_name} Department")
                self.save_data_to_csv()
                break
        else:
            print(f"Student with ID {student_id} was not found.")

    def delete_faculty(self, faculty_id: str):
        for faculty in self.faculty:
            if faculty.faculty_id == faculty_id:
                self.faculty.remove(faculty)
                print(f"Faculty '{faculty.faculty_name}' deleted from '{self.department_name}'")
                self.save_data_to_csv()
                break
        else:
            print(f"Faculty with ID {faculty_id} was not found.")
