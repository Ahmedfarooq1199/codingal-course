
binary = input("Enter a binary number: ")

decimal = 0
length = len(binary)


for i in range(length):
    
    digit = binary[i]
    
  
    if digit != '0' and digit != '1':
        print("Invalid binary number!")
        break
    
    
    power = length - i - 1
    
    
    decimal = decimal + int(digit) * (2 ** power)

else:
    print("Decimal value is:", decimal)