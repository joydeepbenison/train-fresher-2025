# Student Management System
# Concepts: List, Tuple, Set, Dict, Lambda, Generator, Exception Handling

# Generator → generates roll numbers automatically
def roll_number(start=1):
    while True:
        yield start
        start =start + 1

roll_gen = roll_number(101)

# Main student database
students = []

# Function to add student
def add_student():
    try:
        name = input("Enter student name: ").strip()
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))

        personal_info = (name, age)

        # Get roll number from generator
        roll_no = next(roll_gen)

        # Dictionary
        student = {
            "roll_no": roll_no,
            "info": personal_info,
            "marks": marks
        }
        students.append(student)

        print(f"Student {name} added with Roll No: {roll_no}")

    except ValueError:
        print("Invalid input! Please enter correct data.")

    finally:
        print("Student add process completed.\n")

# Function to display students
def display_students():
    if not students:
        print("No students found!\n")
        return

    #Set (unique roll numbers)
    roll_set = {s['roll_no'] for s in students}

    print("\n---- Student Records ----")
    for s in students:
        print(f"Roll No: {s['roll_no']}, Name: {s['info'][0]}, Age: {s['info'][1]}, Marks: {s['marks']}")

# Function to find top student using Lambda + max()
def top_student():
    if not students:
        print("No students available.\n")
        return
    topper = max(students, key=lambda s: s['marks'])
    print(f"Topper: {topper['info'][0]} (Marks: {topper['marks']})\n")

#Main Menu
def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Show Top Student")
        print("4. Exit")

        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                add_student()
            elif choice == 2:
                display_students()
            elif choice == 3:
                top_student()
            elif choice == 4:
                print("Exiting program... Bye!")
                break
            else:
                print("Invalid choice! Please select 1-4.")

        except ValueError:
            print("Enter a valid number!")

# Run the program
if __name__ == "__main__":
    main()

