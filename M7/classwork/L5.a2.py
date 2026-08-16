def factorial(n):
    if n<0:
        return("Invalid Entry")
    elif n==1:
        return(1)
    
    return(n*factorial(n-1))
n = int(input("Enter a number"))
factorial_ = factorial(n)
try :
    print("%d! = %d"%(n,factorial_))

except:
    print(factorial_)
