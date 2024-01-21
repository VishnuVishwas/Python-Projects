# faculty.py

class Faculty:

    def __init__(self, faculty_id: str, faculty_name: str, salary: str, department_id: str) -> None:
        self.faculty_id = faculty_id
        self.facutly_name = faculty_name
        self.salary = salary
        self.department_id = department_id

    # display faculty detials
    def display_faculty_info(self):
        print(f"\nFacutly details:\nFacutly ID: {self.faculty_id}\nName: {self.facutly_name}\nSalary: {self.salary}\nDepartment ID: {self.department_id}")
    
if __name__ == "__main__":
    faculty = Faculty('2', 'vishnu', '001', '10')
    faculty.faculty_info()