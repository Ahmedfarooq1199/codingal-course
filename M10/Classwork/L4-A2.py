print("program to print the factors of a number:")
n = int(input("Enter your number to find it's factors:"))
for i in range(1, n+1):
    if n % i == 0:
        print(i)
        