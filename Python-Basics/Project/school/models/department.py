# department

class Department:

    list_of_departments = ['Science', 'Maths', 'Social', 'Languages']

    def __init__(self, department_id: int, department_head: str) -> None:
        self.department_id = department_id
        self.department_name = self.list_of_departments[department_id]
        self.department_head = department_head
        
    # department info
    def display_department_info(self):
        print(f"\nDepartment details:\nDepartment ID: {self.department_id}\nName: {self.department_name}\nHead of Department: {self.department_head}")

if __name__ == '__main__':
    department = Department(1, 'Gojo')
    department.department_info()

    
        