n = int(input("Enter you number: "))
temp = n
rev_num = 0

while n > 0:
    digit = n % 10
    rev_num = rev_num * 10 + digit
    n = n // 10

if temp == rev_num:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")