# main.py
from models.department import Department

if __name__ == "__main__":
    departments = {}

    while True:
        print("\nSchool Management System")
        print("1. Admit Student")
        print("2. Admit Faculty")
        print("3. Create Course")
        print("4. Display Information")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            # Admit Student
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            department_name = input("Enter department name: ")

            if department_name not in departments:
                departments[department_name] = Department(department_name)

            departments[department_name].admit_student(student_id, student_name)

        elif choice == 2:
            # Admit Faculty
            faculty_id = input("Enter faculty ID: ")
            faculty_name = input("Enter faculty name: ")
            department_name = input("Enter department name: ")

            if department_name not in departments:
                departments[department_name] = Department(department_name)

            departments[department_name].admit_faculty(faculty_id, faculty_name)

        elif choice == 3:
            # Create Course
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            department_name = input("Enter department name: ")

            if department_name in departments:
                departments[department_name].create_course(course_id, course_name)
            else:
                print(f"Error: Department '{department_name}' not found. Please admit the student to the department first.")

        elif choice == 4:
            # Display Information
            print("\nDisplaying Information:")
            if not departments:
                print("No departments found.")
            else:
                for department_name, department in departments.items():
                    print(f"\nDepartment: {department_name}")

                    # Display information about students
                    print("Students:")
                    if not department.students:
                        print("No students found.")
                    else:
                        for student in department.students:
                            print(f"- {student}")

                    # Display information about faculty
                    print("\nFaculty:")
                    if not department.faculty:
                        print("No faculty found.")
                    else:
                        for faculty in department.faculty:
                            print(f"- {faculty}")

                    # Display information about courses
                    print("\nCourses:")
                    if not department.courses:
                        print("No courses found.")
                    else:
                        for course in department.courses:
                            print(f"- {course}")

        elif choice == 5:
            # Quit
            print("Exiting the School Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
