
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print("\nBefore swapping:")
print("a =", a, "b =", b)


temp = a
a = b
b = temp

print("\nAfter swapping using a temporary variable:")
print("a =", a, "b =", b)


a = a + b
b = a - b
a = a - b

print("\nAfter swapping using arithmetic operators:")
print("a =", a, "b =", b)

a, b = b, a

print("\nAfter swapping using tuple unpacking:")
print("a =", a, "b =", b)
