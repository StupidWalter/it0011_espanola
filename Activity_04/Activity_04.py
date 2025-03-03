import csv

students = []
try:
    with open('Activity_04\\record.csv', "r", newline="") as file:
        reader = csv.reader(file)
        students = [tuple(row) for row in reader]
except:
    print("File not found. Starting with an empty record.")

while True:
    print("\nStudent Record Management System")
    print("1. Save File")
    print("2. Show All Students Record")
    print("3. Order by Last Name")
    print("4. Order by Grade")
    print("5. Show Student Record")
    print("6. Add Record")
    print("7. Edit Record")
    print("8. Delete Record")
    print("9. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        with open('Activity_04\\record.csv', "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(students)
    elif choice == "2":
        for student in students:
            print(student)
    elif choice == "3":
        temp_list = list(students)
        temp_list.sort()
        students = tuple(temp_list)
        for student in students:
            print(student)
    elif choice == "4":
        temp_list = list(students)
        temp_list.sort(reverse=True)
        students = tuple(temp_list)
        for student in students:
            print(student)
    elif choice == "5":
        student_id = input("Enter Student ID: ")
        for student in students:
            if student[0] == student_id:
                print(student)
                break
        else:
            print("Student not found.")
    elif choice == "6":
        student_id = input("Enter Student ID: ")
        full_name = input("Enter Full Name: ")
        class_standing = input("Enter Class Standing: ")
        major_exam = input("Enter Major Exam Grade: ")
        temp_list = list(students)
        temp_list.append((student_id, full_name, class_standing, major_exam))
        students = tuple(temp_list)
    elif choice == "7":
        student_id = input("Enter Student ID: ")
        temp_list = list(students)
        for i in range(len(temp_list)):
            if temp_list[i][0] == student_id:
                full_name = input("Enter New Name: ")
                class_standing = input("Enter New Class Standing: ")
                major_exam = input("Enter New Major Exam Grade: ")
                temp_list[i] = (student_id, full_name, class_standing, major_exam)
                break
        else:
            print("Student not found.")
        students = tuple(temp_list)
    elif choice == "8":
        student_id = input("Enter Student ID to delete: ")
        temp_list = [s for s in students if s[0] != student_id]
        students = tuple(temp_list)
    elif choice == "9":
        break
    else:
        print("Invalid choice, please try again.")