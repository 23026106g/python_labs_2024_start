import json

# Step 2: Open and read the students.json file
with open('students.json', 'r') as file:
    data = json.load(file)

# Step 4: Iterate through the list of students and print their details
for student in data['students']:
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Grades: {student['grades']}")
    print()  # Print a blank line for better readability

    #print second student's name   only
    if student['id'] == 2:
        print(f"Name of student with ID 2: {student['name']}")
        break   # Break the loop after finding the student with ID 2    


# print first student's name only
print(f"Name of student with ID 1: {data['students'][0]['name']}")    