while True:
    print("Enter students Details ---")
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    roll_no = input("Enter the Roll Number: ")
    class_name = input("enter the class: ")
    
    Data_Structure = int(input("Enter the marks of DSA: "))
    Compiler_Design = int(input("Enter the marks of Compiler Design: "))
    Operating_System = int(input("Enter the marks of OS: "))
    
    total_marks = Data_Structure + Compiler_Design + Operating_System
    record = (
        f"ID: {student_id}, Name: {name}, Roll No: {roll_no}, class: {class_name},"
        f"Data Structure: {Data_Structure}, Compiler Design: {Compiler_Design}, Operating System: {Operating_System},"
        f"Total : {total_marks}\n"
    )
    
    with open("D:\Error\students.txt.txt", "a") as f:
        f.write(record)
    
    print(" Student record saved!")
    
    more = input("Do you want to add another student? (yes/no)")
    if more.lower() != "yes":
        break
print("\n All records saved in students.txt")
