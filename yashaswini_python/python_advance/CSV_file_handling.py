import csv

# Writing CSV
with open("students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Age", "Grade"])
    writer.writeheader()
    writer.writerow({"Name": "Alice", "Age": 20, "Grade": "A"})
    writer.writerow({"Name": "Bob", "Age": 18, "Grade": "B"})

# Reading CSV
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

