# Faculty class

class Faculty():
    
    def __init__(self, faculty_id: str, faculty_name: str) -> None:
        self.faculty_id = faculty_id
        self.faculty_name = faculty_name
        
    # show faculty details
    def __str__(self):
        return f"Faculty ID: {self.faculty_id}\nName: {self.faculty_name}"