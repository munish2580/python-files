def factorial(n):

    # base case
    if n==0 :
        return 1
    

    # recursive case
    ans= n * factorial(n-1)
    return ans

n=int(input("enter n:"))
print(factorial(n))

