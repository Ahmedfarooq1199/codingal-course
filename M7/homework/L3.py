# swap_numbers.py
# Simple program to swap two numbers

def swap_numbers(a, b):
    print("Before swapping:")
    print("a =", a, "b =", b)

    
    a, b = b, a

    print("After swapping:")
    print("a =", a, "b =", b)

if __name__ == "__main__":
    
    a = int(input("Enter first number (a): "))
    b = int(input("Enter second number (b): "))

    swap_numbers(a, b)
