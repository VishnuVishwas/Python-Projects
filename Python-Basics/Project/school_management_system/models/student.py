# Student class
class Student():
    
    def __init__(self, roll_no: str, student_name: str) -> None:
        self.roll_no = roll_no
        self.student_name = student_name
        
    # show student details
    def __str__(self):
        return f"Student rollno: {self.roll_no}\nName: {self.student_name}"