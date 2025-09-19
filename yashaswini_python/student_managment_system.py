def input_student_details():
    # All student details in one dictionary
    student = {
        "ID": input("Enter Student ID: "),
        "Name": str(input("Enter Student Name: ")),   # explicitly string
        "Roll No": input("Enter Roll Number: "),
        "Class": input("Enter Class: "),
        "English Marks": int(input("Enter English Marks: ")),
        "Hindi Marks": int(input("Enter Hindi Marks: "))
    }
    # Add total marks
    student["Total Marks"] = student["English Marks"] + student["Hindi Marks"]
    return student

def save_to_file(student, filename="student_details.txt"):
    with open(filename, "a") as file:
        for key, value in student.items():   # write each detail in file
            file.write(f"{key}: {value}\n")
        file.write("-" * 20 + "\n")          # separator line

def main():
    print("Student Management System")
    n = int(input("Enter number of students: "))   # ask how many students
    for _ in range(n):
        student = input_student_details()
        save_to_file(student)
        print(f"Details of {student['Name']} saved successfully!\n")

if __name__ == "__main__":
    main()
