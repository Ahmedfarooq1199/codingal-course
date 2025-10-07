
num = int(input("Enter a number: "))


original_num = num


sum_of_powers = 0


num_digits = len(str(num))


while num > 0:
    digit = num % 10
    sum_of_powers += digit ** num_digits
    num //= 10


if original_num == sum_of_powers:
    print(original_num, "is an Armstrong number.")
else:
    print(original_num, "is not an Armstrong number.")
