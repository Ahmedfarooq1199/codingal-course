

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swap:")
print("a =", a)
print("b =", b)


a = a ^ b
b = a ^ b
a = a ^ b

print("\nAfter swap:")
print("a =", a)
print("b =", b)

input("\nPress Enter to exit...")