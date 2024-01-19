import json

student_details = {
    "Name": input("Enter student name: "),
    "ID": int(input("Enter student ID: ")),
    "course": input("Enter student course: ")
}

with open('StudentJson.json', 'w') as json_file:
    json.dump(student_details, json_file, indent=4)

print("Student details written to StudentJson.json successfully.")

with open('StudentJson.json', 'r') as json_file:
    data = json.load(json_file)

print("\nDetails of the Student are")
print("\tName:", data["Name"])
print("\tID:", data["ID"])
print("\tcourse:", data["course"])

course_details = {
    "CourseDetails": {
        "Group": "A",
        "Year": 2
    }
}

data.update(course_details)

with open('StudentJson.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("\nCourseDetails appended and updated in StudentJson.json successfully.")

with open('StudentJson.json', 'r') as json_file:
    updated_data = json.load(json_file)

print("\nDetails of the Student are")
print("\tName:", updated_data["Name"])
print("\tID:", updated_data["ID"])
print("\tcourse:", updated_data["course"])
print("\tGroup:", updated_data["CourseDetails"]["Group"])
print("\tYear:", updated_data["CourseDetails"]["Year"])