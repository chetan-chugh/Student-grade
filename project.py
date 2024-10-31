#Initialising dictionary
student_grades = { }

#Add a new students
def add_student(name, grade):
    student_grades[name] = grade
    #[rahul] = 100
    print(f"Added {name} wih a {grade}")

#Update a student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name} with marks are updated {grade}")

    else:
        print(f"name is not found!")

#delete a student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted")

    else:
        print(f"{name} is not found!")

#View all students
def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")

    else:
        print("No students found/added")

def start():
    while True:
        print("\n Student Grades Managment System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit")

        choice = int(input("Enter Your Choice = "))
        if choice == 1:
            name = input("Enter Student name = ")
            grade = int(input("Enter student grade = "))
            add_student(name, grade)

        elif choice == 2:
            name = int(input("Enter Student name = "))
            grade = int(input("Enter Student grade = "))
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter student name =")
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid choice")

start()