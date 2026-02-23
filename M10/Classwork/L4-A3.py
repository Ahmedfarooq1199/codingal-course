n = input("Enter a Roman numeral: ")
roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
res = 0
for i in range(0,len(roman)-1):
    if roman[n[i]] < roman[n[i+1]]:
        res =res - roman[n[i]]
    else:
        res = res + roman[n[i]]
    
print(res + roman[n[-1]])