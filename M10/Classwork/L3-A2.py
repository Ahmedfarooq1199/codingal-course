def sum(n):
    return n*(n+1)/2

#Space complexity: O(1), Auxiliary space= o(1) 'time complexity: O(1)

def arraysum(a):
    sum=0
    for i in a:
        sum = sum + i 

    return(sum)

a = [12, 3, 4, 15]
arraysum(a)

#Space complexity: 0(n),Auxiliary = 0(1), Time complexity: 0(n)


def summ(n):
    if(n<=0):
        return
    return n+ summ(n-1)


#Space complexity: 0(n),Auxiliary = 0(n), Time complexity: 0(n)


