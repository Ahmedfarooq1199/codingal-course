

print("Hello, Python World!")

name = "Ahmed"
age = 20
is_student = True

print("Name:", name)
print("Age:", age)
print("Student:", is_student)

print("\nData Types:")
print(type(name))
print(type(age))
print(type(is_student))

print("\nSimple Math:")
x = 10
y = 3
print("Addition:", x + y)
print("Division:", x / y)
print("Power:", x ** y)

print("\nLists:")
colors = ["Red", "Green", "Blue"]
print("Colors:", colors)
colors.append("Yellow")
print("Updated Colors:", colors)

print("\nDebugging with pdb:")
import pdb

a = 5
b = 0
# pdb.set_trace()

if b == 0:
    print("Cannot divide by zero!")
else:
    print("Division:", a / b)

print("\nEnd of Intro!")
