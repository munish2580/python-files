# # # creating string
# # name1='college wallah'
# # name2="gkophsdj"
# # name3='''mba 
# # wajwhhj'''

# # print(name1,name2,name3)
# # print(type(name1))
# # print(type(name2))
# # print(type(name3))
# # # indexing in string
# # print(name1[3])

# # # traversing string
# # # using for loop
# # for i in name1:
# #     print(i)


# # # using list comprehension
# # list=[char for char in name1]
# # print(i)

# # # find the length in string
# # print(len(name2))


# # # fiind the  char/substring in string
# # print(name1.find('e'))

# # # slicing in string
# # print(name1[8:11])


# # for converting char to upper case
# str1="new york"
# str2=str1.upper()
# print(str2)

# # for converting char to lower case
# str3=str2.lower()
# print(str3)

# # for capitalising the first chr of ny string 
# str4=str3.capitalize()
# print(str4)


# for stripping/removeing any trailing whitespace
# str1="    hello   world   "
# print(str1.strip())
# print(str1)

# replacing substring
# str1="hello world,what  world ndsof mwknf dkeknf"
# print(str1.replace("world","earth",1))

# spiliting string
# str1="ria, pia, tia ,via ,mia"
# list=str1.split(",",2)
# print(list)

# concatenaton 
# str1="hello world"
# str2="fhhdoqdjcicoiec"
# print(str1+str2)


# formating string
student="paro"
marks=98
str1= "the student name is {s}, and marks is {m}".format(s = student,m = marks)
print(str1)