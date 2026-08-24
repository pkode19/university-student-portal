# University Student Portal
# Developer A - Student Registration and Generated Email

# Collect student information
full_name = input("Enter your full name: ")
student_id = input("Enter your student ID: ")
programme = input("Enter your programme: ")
level = input("Enter your level: ")
age = input("Enter your age: ")
hall = input("Enter your hall of residence: ")

# Generate student email using string concatenation
name_part = full_name[:3].lower()
student_email = name_part + student_id + "@st.ug.edu.gh"

# Build the border using string concatenation
border_part = "=========="
border = border_part + border_part + border_part + border_part + border_part

# Display student profile
print()
print(border)
print("             UNIVERSITY STUDENT PORTAL")
print(border)
print()
print("Student Profile")
print()
print("Full Name          : " + full_name)
print("Student ID         : " + student_id)
print("Programme          : " + programme)
print("Level              : " + level)
print("Age                : " + age)
print("Hall               : " + hall)
print("Generated Email    : " + student_email)
print()
print(border)
print("              UNIVERSITY OF GHANA")
print(border)