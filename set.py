# name={"sia","tia","mia"}
# print(name)
# print(len(name))
# print(type(name))
# for x in name :
#     print(x)

# if "sia" in name:
#     print("sia in the set")   
# else:
#     print("your name is not in set")

#     #add in element in set
# name.add("sia")
# print(name)

# #add another name in set
# names_list=["ria","kia"]
# name.update(names_list)
# print(name)

# #removing element from set
# # name.remove("ria")
# name.discard("ria")
# print(name)

#joining two sets 
s1={"a","b","c"}
s2={"d","e","a"}
print(s1,s2)

# s3=s1.union(s2)
# print(s3)

# s1.update(s2)
# print(s1)

#keep only duplicates while joining
# s1.intersection_update(s2)
# print(s1)

#keep all values expect duplictes
s1.symmetric_difference_update(s2)
print(s1)