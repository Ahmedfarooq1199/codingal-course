print("program to check whether the number is given is prime numberor not")
flag = True
n = int(input("Enter the number: "))
for i in range(2, n):
    if n % i == 0:
        flag = False
        break
    else:
        flag = True

if flag== True:
    print("The number is prime")
else:
    print("The number is not prime")
