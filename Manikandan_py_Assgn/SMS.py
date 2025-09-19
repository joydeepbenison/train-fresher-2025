""" Design a student management system , which can input a students id , name , roll no , class ,
Marks obtained , save .txt file
"""
 
# Function to get one student's details from user
def get_student_info():
    student = {}
    student['id'] = int(input("Enter student id: "))
    student['name'] = input("Enter student name: ")
    student['roll_no'] = int(input("Enter student roll no: "))
    student['class'] = input("Enter student class: ")
    student['marks1'] = float(input("Enter marks obtained in English: "))
    student['marks2'] = float(input("Enter marks obtained in Math: "))
    return student
 
 
# Function to save one student's details to file
def save_to_file(student):
    with open("student_data.txt", "a") as file:
        file.write(
            f"ID: {student['id']}\n"
            f"Name: {student['name']}\n"
            f"Roll No: {student['roll_no']}\n"
            f"Class: {student['class']}\n"
            f"English Mark: {student['marks1']}\n"
            f"Maths Mark: {student['marks2']}\n\n"
        )
 
 
# Main function
def main():
    n = int(input("Enter number of students: "))
    for _ in range(n):
        student = get_student_info()
        save_to_file(student)
    print(" ....student details saved to student_data.txt..... ")
 
 
# Start the program
if __name__ == "__main__":
    main()
