n = int(input(" Enter the number:"))

digits = len(str(n))

sum = 0
temp = n

while temp > 0:
    d = temp % 10
    sum = sum + d ** digits
    temp = temp // 10

if n == sum:
    print(n, "is an armstrong number")
else:
    print(n, "is not a armstrong number")