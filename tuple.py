# creating a tuple
colours=("red","yellow","green")

#  creating a tuple with 1 items
# fruit=("apple",)
fruit=tuple(("apple"))

# check a type tuple
print(type(fruit))

# check the length of tuole 
print(len(colours))

# accessing item in tuple
print(colours[1])   #+sitive indexing
print(colours[-2])  #-itive  indexing
print(colours[1:3])  #range indexing
print(colours[-2:])  #negtive range indexing 

#check if an exists in tuple 
if  "green" in colours:
    print("green is part of tuple")

# traverse the tuple
for i in colours:
    print(i) 

#concatenate 2 tuple
more_colour=("blue","brown")
colours=colours + more_colour
print(colours)

#unpacking a tuple
# colour1, colour2, colour3= colours
# print(colour1,colour2,colour3)


#reverse tuple
n=(1,2,3,4,5,6)
list=[]
for x in reversed (n): 
    list.append(x)

output=tuple(list)
print(output)

