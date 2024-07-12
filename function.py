# writing func  for calu sum 1 to n
def sumonetoN(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum   
 
n=int(input("enter n:"))
#  call funtion
output=sumonetoN(n)
print("the sum of all numbers till n is:",output)  
  
n1=int(input("enter n:"))
output1=sumonetoN(n1)

print("the sum of all numbers till n is:",output1)  
