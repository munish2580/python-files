a="aabcccccaaa"
list=[]
count=1
list.append (a[0])
for i in range(1 , len (a)):
    if (a[i]==a[i-1]):
        count+=1
    else:
        list.append(str(count))
        list.append(a[i])
        count=1
list.append(str(count))
list="".join(list)
print ("your string is \"aabcccccaaa\"")
print (f"The compressed string is: {list}")
