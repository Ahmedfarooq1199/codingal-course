
print("For loop example:")
for i in range(1, 6):  
    print("Number:", i)

print("\nFor loop with a list:")
fruits = ["Apple", "Banana", "Cherry", "Mango"]
for fruit in fruits:
    print("I like", fruit)


print("\nWhile loop example:")
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

print("\nWhile loop with break:")
num = 1
while True:  
    print("Number:", num)
    if num == 3:  
        break
    num += 1
