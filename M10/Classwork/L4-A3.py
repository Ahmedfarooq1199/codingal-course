# Program to convert roman numerals to integers

def romanToInt(n):
    roman = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    res = 0
    n = n.upper()   # Convert to uppercase

    for i in range(len(n) - 1):
        if roman[n[i]] < roman[n[i + 1]]:
            res -= roman[n[i]]
        else:
            res += roman[n[i]]

    return res + roman[n[-1]]


# Take roman as input from user
n = input("Input roman numeral: ")

# Check if input is empty
if n:
    print("Integer equivalent:", romanToInt(n))
else:
    print("Invalid input!")