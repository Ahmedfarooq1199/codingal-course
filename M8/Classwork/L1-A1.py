lst = ['Apple', 'Guava', 'Mango', 'banana', 'Elderberry']

print("length of the list:", len(lst))
print("first Element:", lst[0])
print("Last Element:", lst[-1])

lst.append('Papaya')
print("Upadted List:", lst)

lst.remove('Guava')
print("Updated List:", lst)

lst.sort()
print("Sorted List:", lst)

lst.pop(1)
print("Updated list :", lst)

lst.reverse()
print("Reversed List:", lst)

lst = lst*2
print("Multiplication of List:", lst)

lst = lst[2:5]
print("Sliced List:", lst)

lst.clear()
print("Updated List:", lst)