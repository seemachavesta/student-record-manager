students = {
    '1': {'name': 'Sona', 'age': 22, 'grades': [90, 55, 88, 90]},
    '2': {'name': 'Maria', 'age': 20, 'grades': [80, 65, 88, 98]},
    '3': {'name': 'Alex', 'age': 27, 'grades': [50, 52, 75, 89]},
    '4': {'name': 'Rexy', 'age': 36, 'grades': [60, 88, 43, 78]},
}


# Calculate the average of grades
def calculate_average(grades):
    if not grades:
        print('No grades available to calculate the average.')
        return None
    return sum(grades) / len(grades)


# Add information to the record
def add_information(student_id, key, value):
  students[student_id][key] = value
  print(f"You have added '{key}: {value}' to the record.")


# Delete a student record
def delete_record(student_id):
    if student_id in students:
        del students[student_id]
        print("Student has been deleted successfully.")
    else:
        print("Student ID not found.")


# Update student grades
def update_grade(grade_value, grades):
    if not isinstance(grades, list):
        print("Grades field is not a list. Initializing it as an empty list.")
        grades = []
    if 0 <= grade_value <= 100:
        grades.append(grade_value)
        print(f"Your grade has been successfully updated. New grades: {grades}")
    else:
        print("Invalid grade. Please enter a value between 0 and 100.")


# Display a student's record
def view_record(student_id):
    if student_id not in students:
        print("Student record not found.")
        return
    record = students[student_id]
    for key, value in record.items():
        print(f"{key}: {value}")
    return record.get('grades', [])


# Validate student ID
def validate_id(student_id):
    if student_id not in students:
        print("Student ID not found. Please try again.")
        return False
    return True


# Options menu
options = """
Options:
1: View Record
2: Add Information
3: Update Grade
4: Calculate Average
5: Delete Record
6: Exit
"""

while True:
    print(options)
    try:
        choice = int(input('Enter your option: '))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
        continue

    if choice == 1:
        student_id = input("Enter your ID to view the student record: ")
        if validate_id(student_id):
            view_record(student_id)

    elif choice == 2:
        student_id = input("Enter your ID to add information: ")
        if validate_id(student_id):
            key = input("What would you like to add: ")
            if key in students[student_id]:
              print(f"{key} already exist in the reocrd.")
              continue
            
            value = input(f"What is your {key}: ")
            add_information(student_id, key, value)

    elif choice == 3:
        student_id = input("Enter your ID to update grades: ")
        if validate_id(student_id):
            try:
                grade_value = int(input("Enter the grade: "))
                update_grade(grade_value, students[student_id]['grades'])
            except ValueError:
                print("Invalid grade. Please enter a numeric value.")

    elif choice == 4:
        student_id = input("Enter your ID to calculate the average grade: ")
        if validate_id(student_id):
            average = calculate_average(students[student_id].get('grades', []))
            if average is not None:
                print(f"Average grade: {average:.2f}")

    elif choice == 5:
        student_id = input("Enter your ID to delete the record: ")
        confirm = input("Are you sure you want to delete this record? (yes/no): ").strip().lower()
        if confirm == 'yes':
            delete_record(student_id)
        else:
            print("Delete operation canceled.")

    elif choice == 6:
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")