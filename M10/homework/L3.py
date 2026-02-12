

n = int(input("Enter a number: "))


print("\nExample 1: O(n) Time, O(1) Space")

for i in range(n):   
    print(i)


print("\nExample 2: O(n) Time, O(n) Space")

arr = []   

for i in range(n):
    arr.append(i)   

print("Array:", arr)

print("\nExample 3: O(n^2) Time, O(1) Space")

for i in range(n):
    for j in range(n):
        print(i, j)

