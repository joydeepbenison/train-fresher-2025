#function to collect students details from user
def get_student_data():
    #basic student information
    s_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    roll = int(input("Enter Roll Number: "))
    student_class = input("Enter Class: ")
    print("Enter marks obtained in each subject:")
    english = int(input("English Marks: "))
    math = int(input("Math Marks: "))
    hindi = int(input("Hindi Marks: ")) 
    total = english + math + hindi

    # Return all data as a dictionary
    return {
        "Student ID": s_id,
        "Name": name,
        "Roll No": roll,
        "Class": student_class,
        "English": english,
        "Math": math,
        "Hindi": hindi,
        "Total": total
    }
#function to save student data to file
def save_student_data(data):
    #open the file
    with open("student_details.txt", "a") as f:
        f.write("Student ID: " + data["Student ID"] + "\n")#write student details in file
        f.write("Name: " + data["Name"] + "\n")
        f.write("Roll No: " + str(data["Roll No"]) + "\n")
        f.write("Class: " + data["Class"] + "\n")
        f.write("Marks Obtained:\n")
        f.write("English: " + str(data["English"]) + "\n")
        f.write("Math: " + str(data["Math"]) + "\n")
        f.write("Hindi: " + str(data["Hindi"]) + "\n")
        f.write("Total: " + str(data["Total"]) + "\n")
        f.write("-" * 20 + "\n")
    print("Details saved")

student_data = get_student_data()#get student details from user
print("Total Marks:", student_data["Total"])
save_student_data(student_data)#save the data to file

