num = int(input("Enter a number to check "))

if num>50:
    print("The number is greater than 50")
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")


else:
    print("The number  less than 50")