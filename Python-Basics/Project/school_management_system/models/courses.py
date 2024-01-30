# Courses
class Courses():
    def __init__(self, course_id: str, course_name: str) -> None:
        self.course_id = course_id
        self.course_name = course_name
    
    # course details
    def __str__(self) -> str:
        return f"Course ID: {self.course_id}\nCourse Name: {self.course_name}"  
    
    