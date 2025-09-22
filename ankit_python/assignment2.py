with open("D:\Error\students.txt.txt", "r") as f:
    lines = f.readlines()

print("Student Records")
for line in lines:
    data = line.strip().split(",")
    print(data)
    
    student_id = data[0].split(":")[1].strip()
    name = data[1].split(":")[1].strip()
    roll_no = data[2].split(":")[1].strip()
    class_name = data[3].split(":")[1].strip()
    Data_Structure = int(data[4].split(":")[1].strip())
    Compiler_Design = int(data[5].split(":")[1].strip())
    Operating_System = int(data[6].split(":")[1].strip())
    
    total_marks = Data_Structure + Compiler_Design + Operating_System
    
    print(f"ID: {student_id}, Name: {name}, Roll: {roll_no}, Class: {class_name}, "
          f"DSA: {Data_Structure}, Compiler: {Compiler_Design}, OS: {Operating_System}, "
          f"Total: {total_marks}")

