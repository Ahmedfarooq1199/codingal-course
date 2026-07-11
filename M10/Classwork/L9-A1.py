a, b = 7,7

print("a ^ a =", a ^ a)
print("a ^ 0 =", a ^ 0)

print("Equal (XOR):", (a ^ b) == 0)

arr = [2, 5, 3, 2, 5, 3, 7]
result = 0
for i in arr:
    result = result ^ i
print("XOR of", arr, "=", result)

nums = [4, 7, 4, 2, 7, 2, 9]
res = 0
for n in nums:
    res = res ^ n
print("Odd occurring element:", res)

list = [3, 9, 3, 5, 5, 7]
res1 = 0
for n in list:
    res1 = res1 ^ n
print("XOR of two odds:", res1)

x = 3
y = 5
xor=x ^ y
rightmost_set_bit = xor & -xor
print(rightmost_set_bit)
