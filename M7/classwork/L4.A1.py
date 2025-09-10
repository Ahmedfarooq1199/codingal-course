num = int(input("Enter a number: "))

print(f"table of {num}")

for i in range(1, 11):
    mul = num*i
    print("%d x %d = %d" % (num, i, mul))
    
