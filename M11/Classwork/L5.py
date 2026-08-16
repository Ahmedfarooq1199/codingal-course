

binary = input("Enter binary clue: ")


if all(bit in "01" for bit in binary):
    decimal = int(binary, 2)
    hexadecimal = hex(decimal)

    print("\nInvestigation Result")
    print("--------------------")
    print("Binary     :", binary)
    print("Decimal    :", decimal)
    print("Hexadecimal:", hexadecimal)

    # Try converting binary into ASCII text
    if len(binary) % 8 == 0:
        text = ""

        for i in range(0, len(binary), 8):
            byte = binary[i:i+8]
            text += chr(int(byte, 2))

        print("ASCII Text :", text)
    else:
        print("ASCII Text : Binary length is not a multiple of 8.")

else:
    print("Invalid binary clue!")
    print("Use only 0 and 1.")

input("\nPress Enter to exit...")