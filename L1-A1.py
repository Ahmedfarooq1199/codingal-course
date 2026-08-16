set = ["A", "B", "C"]

n = len(set)
total_subsets = 2 ** n

print("Set Items:", set)
print("Total Subsets: 2 ^", n, "=", total_subsets)


print(" Creating mask table for ",n)
count = 0
while count < total_subsets:
    bit2 =  (count >> 2) & 1
    bit1 =  (count >> 1) & 1
    bit0 =  count & 1
    print("  mask ->",count,":", bit2, bit1, bit0)
    count = count + 1

m = 0
while m < total_subsets:
    sub = []
    j = 0
    while j < n:
        p = 1 << j
        if m & p:
            sub.append(set[j])
        j = j + 1

    print("Subset ->", m, ":", sub)
    m = m + 1
