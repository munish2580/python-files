n= int (input("enter n :"))

for i in range(n):  #loops for rows
    for j in range(1,n+1):  #loops for column
        print(j ,end="")
    print()


n= int (input("enter n :"))
for  i in range(1,n+1):  #loops for rows
    for j in range(1,i+1):  #loops for column
        print(j ,end="")
    print()


n = int(input("enter the number:"))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(ord('A') + j), end="")
    print()


n=int (input("enter n:"))

for i  in range (1, n+1):
    print(" " * (n-i),end="")

    for j in range(1, 2*i):
        print(j,end="")
    print()
