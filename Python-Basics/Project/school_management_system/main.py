from models.department import Department, Student, Faculty, Courses

departments = {}

# Assuming these are the available departments
available_departments = ['CSE', 'ECE']

while True:
    print("\nSchool Management System")
    print("1. Admit Student")
    print("2. Admit Faculty")
    print("3. Create Course")
    print("4. Display Information")
    print("5. Update Student Details")
    print("6. Update Faculty Details")
    print("7. Delete Student")
    print("8. Delete Faculty")
    print("9. Quit")

    department_name = input("Choose department from {CSE, ECE}: ")

    if department_name not in available_departments:
        print(f"Error: Invalid department name. Choose from {available_departments}")
        continue

    if department_name not in departments:
        departments[department_name] = Department(department_name)

    choice = input("Enter your choice (1-9): ")

    try:
        choice = int(choice)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        departments[department_name].admit_student(student_id, student_name)

    elif choice == 2:
        faculty_id = input("Enter faculty ID: ")
        faculty_name = input("Enter faculty name: ")
        departments[department_name].admit_faculty(faculty_id, faculty_name)

    elif choice == 3:
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        departments[department_name].create_course(course_id, course_name)

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
        # Update Student Details
        student_id = input("Enter student ID: ")
        new_name = input("Enter new student name: ")
        departments[department_name].update_student_details(student_id, new_name)

    elif choice == 6:
        # Update Faculty Details
        faculty_id = input("Enter faculty ID: ")
        new_name = input("Enter new faculty name: ")
        departments[department_name].update_faculty_details(faculty_id, new_name)

    elif choice == 7:
        # Delete Student
        student_id = input("Enter student ID: ")
        departments[department_name].delete_student(student_id)

    elif choice == 8:
        # Delete Faculty
        faculty_id = input("Enter faculty ID: ")
        departments[department_name].delete_faculty(faculty_id)

    elif choice == 9:
        # Quit
        for department in departments.values():
            department.save_data_to_csv()
        print("Exiting the School Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 9.")
