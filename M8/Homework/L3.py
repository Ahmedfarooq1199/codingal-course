
from datetime import date


today = date.today()


name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))


age = today.year - birth_year

print("\n--- Exam Eligibility Check ---")
print(f"Name: {name}")
print(f"Age: {age}")

if age >= 18:
    print("You are eligible to appear in the exam.")
elif 16 <= age < 18:
    print("You are eligible for the exam with parental permission.")
else:
    print("You are not eligible to appear in the exam.")
