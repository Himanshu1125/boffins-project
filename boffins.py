def fact(n):
    if(n==0 or n==1):
        return n
    else:
        return n * fact(n-1)

n=5 
result=fact(n)
print("factorial of",n,"is",result)