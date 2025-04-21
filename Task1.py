#Task 1: Create a Dictionary of Student Marks

marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90,
    "Ethan": 88
}

student = input("Enter the student's name: ").title()

if student in marks:
    print(f"{student}'s marks are {marks[student]}.")
else:
    print(f"Student '{student}' not found in the records.")

