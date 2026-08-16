def lcm(a, b):
    greater = max(a, b)

    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = lcm(num1, num2)

print("LCM =", result)

input("\nPress Enter to exit...")