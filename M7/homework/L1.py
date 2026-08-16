# beginner.py
# A very simple Python program for beginners

# Print a welcome message
print("👋 Welcome to Python Basics!")

# Variables
name = input("What is your name? ")
age = int(input("How old are you? "))

# Simple math
next_year_age = age + 1

# If/Else example
if age < 18:
    print(f"Hello {name}, you are still a minor. Next year you will be {next_year_age}.")
else:
    print(f"Hello {name}, you are an adult. Next year you will be {next_year_age}.")

# Loop example
print("\nLet's count to 5:")
for i in range(1, 6):
    print(i)

# Function example
def greet(person):
    return f"Nice to meet you, {person}!"

print(greet(name))

print("\n🎉 Program finished. Great job learning Python!")
