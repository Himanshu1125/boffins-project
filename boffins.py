def fact(n):
    if(n==0 or n==1):
        return n
    else:
        return n*fact(n-1)
    
n = 5
print("Factorial of",n," is ", fact(n))