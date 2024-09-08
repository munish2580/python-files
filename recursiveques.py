# # def printnto1(n):

# #     # base case
# #     if n==0:
# #         return 
    
# #     # print (n)

# #     # recursive case
# #     printnto1(n-1)
# #     print(n)

# # printnto1(7)


# # # sum of 1 to n in  recursive 
# # def sum(n):

# #     # base case
# #     if n==1:
# #         return 1
    

# #     # recursive case
# #     ans=n+sum(n-1)
# #     return ans

# # n=int(input("enter n:"))
# # print(sum(n))
        

# # power resied a to b in recusive 
# def power(a,b):

#     # base case
#     if b==0:
#         return 1
    
#     # recursive case
#     ans=a *power(a,b-1)
#     return ans 

# a=int(input("enter a:"))
# b=int(input("enter b:"))
# print(power(a,b))



# fibonacci sequence
def fibonacci(n):

    # base case
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
    

n=int(input("enter n:"))
for i in range(1,n+1):
   print(fibonacci(i ))    
        
