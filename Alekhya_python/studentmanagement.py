student = int(input("enter number of students: "))

for i in range(student):
    print("\nStudent", i + 1)

    s_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    roll = int(input("Enter Roll Number: "))
    student_class = input("Enter Class: ")
    print("enter marks obtained in each subject")
    english = int(input("English Marks: "))
    math = int(input("Math Marks: "))
    hindi = int(input("Hindi Marks: "))
    total = english + math + hindi
    print("Total Marks:", total)

    with open("student.txt", "a") as f:
        f.write("Student ID: " + s_id + "\n")
        f.write("Name: " + name + "\n")
        f.write("Roll No: " + str(roll)+ "\n")
        f.write("Class: " + student_class + "\n")
        f.write("Marks Obtained:\n")
        f.write("English: " + str(english) + "\n")
        f.write("Math: " + str(math) + "\n")
        f.write("Hindi: " + str(hindi) + "\n")
        f.write("Total: " + str(total) + "\n")
        f.write("-" * 20 + "\n")
        print("Details saved")
