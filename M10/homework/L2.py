

n = int(input("Enter a number: "))


print("\nLinear Loop O(n):")
for i in range(n):
    print("Hello")


print("\nNested Loop O(n^2):")
for i in range(n):
    for j in range(n):
        print("Hi")


print("\nLogarithmic Loop O(log n):")
i = 1
while i < n:
    print("Hey")
    i = i * 2
