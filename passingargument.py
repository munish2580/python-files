# pass by value
def addone(x):
    x=x+1
    print("inside function:",x)


x=5
addone(x) 
print("outside function:",x) 

# pass by reference
def modifylist(list):
    # list.append(4)
    list=[4,5,6]
    print("inside function:",list)

list=[1,2,3]
modifylist(list) 
print("outside function:",list)   