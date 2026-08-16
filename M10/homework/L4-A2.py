

number = int(input("Enter a number (0-255): "))

binary = format(number, '08b')

print("\nSwitch Status:")
for i in range(8):
    if binary[i] == '1':
        print(f"Switch {7-i}: ON")
    else:
        print(f"Switch {7-i}: OFF")

print("\nBinary Value:", binary)