n = 52 
def bits(n):
    return bin (n)[2:]
print("n =", n, "->", bits(n))
print("Set bits in", n, "->", bits(n).count('1'))
print("Zero set bits in", n, "->", bits(n).count('0'))

pos = 1
temp=n 
while temp:
    if temp & 1:
        break
    pos = pos + 1
    temp >>= 1
print("First set bit of", n, "-> position", pos)


print( "checking set bit and not set bit ")
for i in range(1, 7):
    if n & (1<< (i - 1)):
        result = "SET"
    else:
        result = "NOT SET"

    print("bit:", i, result)
