# Smart Light Control using Simple Reflex Agent

is_daylight_there = input("Is daylight there? (yes/no): ").lower()
is_human_there = input("Is human present? (yes/no): ").lower()

if is_daylight_there == "no" and is_human_there == "yes":
    print("Light ON")
else:
    print("Light OFF")


# Attendance Decision Agent

is_teacher_there = input("Is teacher there? (yes/no): ").lower()
is_student_there = input("Is student there? (yes/no): ").lower()

if is_teacher_there == "yes" and is_student_there == "no":
    print("Attendance granted")
else:
    print("No Attendance")

# Medical Specialist Decision Agent

eye_issue = input("Do you have an eye issue? (yes/no): ").upper()
skin_issue = input("Do you have a skin issue? (yes/no): ").upper()

if eye_issue == "YES" and skin_issue == "NO":
    print("Go to ophthalmologist")
elif eye_issue == "NO" and skin_issue == "YES":
    print("Go to dermatologist")
elif eye_issue == "YES" and skin_issue == "YES":
    print("Consult both ophthalmologist and dermatologist")
else:
    print("Think yourself!!!")

