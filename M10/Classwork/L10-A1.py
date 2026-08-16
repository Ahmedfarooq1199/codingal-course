
from ast import If


n = 12

res = n & (n - 1)
print("After AND operator:", res)
print(bin(res))

x = int(input("Enter the number:"))
if x & (x-1) == 0:
    print("its a power of 2")
else:
    print("its not a power of two")

y = int(input("Enter the number:"))

def isPowerOfFour(y):
    while y > 1:
        if y % 4 != 0:
            return False
        y = y // 4
    return y == 1

if isPowerOfFour(y):
    print("Given number is power of four")
else:
    print("Given number is not a power of four")


num = int(input("Enter a number:"))
def is_power_of_8(n):
    if(n & (n - 1)) != 0:
        return False
    count = 0
    while n > 1:
        n >>= 1
        count = count + 1
    return count % 3 == 0

if is_power_of_8(num):
    print("Given number is power of eight")
else:
    print("Given number is not a power of eight")